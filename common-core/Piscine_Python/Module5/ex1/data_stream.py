from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union


Stats = Dict[str, Union[str, int, float]]


@dataclass
class StreamStats:
    stream_id: str
    processed_batches: int = 0
    processed_items: int = 0
    errors: int = 0

    def as_dict(self) -> Stats:
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
            "processed_items": self.processed_items,
            "errors": self.errors,
        }


class DataStream(ABC):
    """Abstract base for polymorphic stream handlers."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self._stats = StreamStats(stream_id=stream_id)

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        raise NotImplementedError

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Default filtering: return input unchanged, unless criteria provided."""
        if criteria is None:
            return list(data_batch)

        crit = criteria.strip().lower()
        if not crit:
            return list(data_batch)

        # Generic default: keep items whose string representation contains criteria
        return [item for item in data_batch if crit in str(item).lower()]

    def get_stats(self) -> Stats:
        """Default stats representation (subclasses may extend)."""
        return self._stats.as_dict()

    def _record_success(self, batch_size: int) -> None:
        self._stats.processed_batches += 1
        self._stats.processed_items += batch_size

    def _record_error(self) -> None:
        self._stats.errors += 1


class SensorStream(DataStream):
    """Stream for environmental sensor readings like 'temp:22.5'."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = self.filter_data(data_batch)
            parsed = [self._parse_reading(x) for x in readings]
            temps = [v for (k, v) in parsed if k == "temp"]
            avg_temp = sum(temps) / len(temps) if temps else 0.0
            self._record_success(len(readings))
            return (
                f"Sensor analysis: {len(readings)} readings processed, "
                f"avg temp: {avg_temp}°C"
            )
        except ValueError as exc:
            self._record_error()
            raise ValueError(f"SensorStream failure: {exc}") from exc

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        readings = [x for x in data_batch if isinstance(x, str)]
        if criteria is None:
            return readings

        crit = criteria.strip().lower()
        if crit == "critical":
            # Example "critical" heuristic: keep readings with "alert" marker.
            return [x for x in readings if "alert" in x.lower()]
        return super().filter_data(readings, criteria)

    @staticmethod
    def _parse_reading(item: str) -> tuple[str, float]:
        if ":" not in item:
            raise ValueError(f"Invalid reading format: {item!r}")
        key_raw, value_raw = item.split(":", 1)
        key = key_raw.strip().lower()
        try:
            value = float(value_raw.strip())
        except ValueError as exc:
            raise ValueError(f"Invalid numeric value in {item!r}") from exc
        return key, value


class TransactionStream(DataStream):
    """Stream for financial operations like 'buy:100' / 'sell:150'."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            ops = self.filter_data(data_batch)
            parsed = [self._parse_op(x) for x in ops]
            net = 0.0
            for kind, amount in parsed:
                if kind == "buy":
                    net -= amount
                elif kind == "sell":
                    net += amount
            self._record_success(len(ops))
            return (
                f"Transaction analysis: {len(ops)} operations, "
                f"net flow: {net} units"
            )
        except ValueError as exc:
            self._record_error()
            raise ValueError(f"TransactionStream failure: {exc}") from exc

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        ops = [x for x in data_batch if isinstance(x, str)]
        if criteria is None:
            return ops

        crit = criteria.strip().lower()
        if crit == "large":
            # Keep operations with abs(amount) >= 100
            kept: list[str] = []
            for item in ops:
                try:
                    _, amount = self._parse_op(item)
                except ValueError:
                    continue
                if abs(amount) >= 100:
                    kept.append(item)
            return kept
        return super().filter_data(ops, criteria)

    @staticmethod
    def _parse_op(item: str) -> tuple[str, float]:
        if ":" not in item:
            raise ValueError(f"Invalid operation format: {item!r}")
        kind_raw, amount_raw = item.split(":", 1)
        kind = kind_raw.strip().lower()
        if kind not in {"buy", "sell"}:
            raise ValueError(f"Unsupported operation kind: {kind!r}")
        try:
            amount = float(amount_raw.strip())
        except ValueError as exc:
            raise ValueError(f"Invalid amount in {item!r}") from exc
        return kind, amount


class EventStream(DataStream):
    """Stream for system events like 'login', 'error', 'logout'."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = self.filter_data(data_batch)
            normalized = [str(x).strip().lower() for x in events]
            error_count = sum(1 for e in normalized if e == "error")
            self._record_success(len(events))
            return (
                f"Event analysis: {len(events)} events, "
                f"{error_count} error detected"
            )
        except Exception as exc:
            self._record_error()
            raise ValueError(f"EventStream failure: {exc}") from exc

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        events = [x for x in data_batch if isinstance(x, str)]
        if criteria is None:
            return events

        crit = criteria.strip().lower()
        if crit == "high":
            # Treat "error" as high priority.
            return [x for x in events if x.strip().lower() == "error"]
        return super().filter_data(events, criteria)


class StreamProcessor:
    """Manager that handles any DataStream subtype polymorphically."""

    def __init__(self) -> None:
        self._streams: list[DataStream] = []

    def register(self, stream: DataStream) -> None:
        self._streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> Dict[str, str]:
        results: Dict[str, str] = {}
        for stream in self._streams:
            batch = batches.get(stream.stream_id, [])
            results[stream.stream_id] = stream.process_batch(batch)
        return results

    def filter_all(
        self,
        batches: Dict[str, List[Any]],
        criteria: str,
    ) -> Dict[str, List[Any]]:
        return {
            stream.stream_id: stream.filter_data(batches.get(stream.stream_id, []),
                                                criteria)
            for stream in self._streams
        }


def _demo() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    manager = StreamProcessor()
    manager.register(sensor)
    manager.register(trans)
    manager.register(event)

    batches: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:22.5", "humidity:65", "pressure:1013"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75"],
        "EVENT_001": ["login", "error", "logout"],
    }

    for s in [sensor, trans, event]:
        print(f"\nInitializing {s.__class__.__name__}...")
        print(f"Stream ID: {s.stream_id}")

    print("\n=== Polymorphic Stream Processing ===")
    results = manager.process_all(batches)
    for stream_id, summary in results.items():
        print(f"{stream_id}: {summary}")

    print("\nStream filtering active: High-priority data only")
    filtered = manager.filter_all(batches, criteria="high")
    for stream_id, data in filtered.items():
        print(f"{stream_id}: {data}")

    print("\nStats:")
    for s in [sensor, trans, event]:
        print(f"{s.stream_id}: {s.get_stats()}")


if __name__ == "__main__":
    _demo()
