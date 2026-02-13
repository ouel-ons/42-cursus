from __future__ import annotations

import json
import time
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Any, Deque, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
    """Duck-typed interface: any class with process(data) can be a stage."""

    def process(self, data: Any) -> Any:
        ...


@dataclass
class PipelineStats:
    pipeline_id: str
    processed: int = 0
    errors: int = 0
    last_duration_s: float = 0.0

    def as_dict(self) -> Dict[str, Union[str, int, float]]:
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self.processed,
            "errors": self.errors,
            "last_duration_s": self.last_duration_s,
        }


class ProcessingPipeline(ABC):
    """Abstract pipeline that composes stages and orchestrates data flow."""

    def __init__(
        self,
        pipeline_id: str,
        stages: Optional[List[ProcessingStage]] = None,
    ) -> None:
        self.pipeline_id = pipeline_id
        self._stages: list[ProcessingStage] = list(stages or [])
        self._stats = PipelineStats(pipeline_id=pipeline_id)
        self._backup_mode = False

    def add_stage(self, stage: ProcessingStage) -> None:
        self._stages.append(stage)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = self._stats.as_dict()
        stats["stages"] = len(self._stages)
        stats["backup_mode"] = int(self._backup_mode)
        return stats

    def run(self, data: Any) -> Any:
        start = time.perf_counter()
        try:
            current = data
            for stage in self._stages:
                current = stage.process(current)
            self._stats.processed += 1
            return current
        except Exception as exc:
            self._stats.errors += 1
            raise ValueError(f"Stage processing failed: {exc}") from exc
        finally:
            self._stats.last_duration_s = time.perf_counter() - start

    def recover(self) -> None:
        """Simple recovery toggle; could swap strategies in real systems."""
        self._backup_mode = True

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Adapter-specific entrypoint (format-specific), to be overridden."""
        raise NotImplementedError


class InputStage:
    """Stage 1: input validation / normalization."""

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Input cannot be None.")
        if isinstance(data, str):
            text = data.strip()
            if not text:
                raise ValueError("Input string cannot be empty.")
            return text
        return data


class TransformStage:
    """Stage 2: transformation / enrichment."""

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            enriched = dict(data)
            enriched.setdefault("meta", {})
            meta = enriched["meta"]
            if isinstance(meta, dict):
                meta.setdefault("validated", True)
                meta.setdefault("source", "nexus")
            return enriched
        if isinstance(data, list):
            return [x for x in data if x is not None]
        return data


class OutputStage:
    """Stage 3: output formatting / delivery."""

    def process(self, data: Any) -> Any:
        # Keep it generic: adapters decide final serialization.
        return data


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON payloads."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, str):
                raise ValueError("JSONAdapter expects a JSON string.")
            parsed = json.loads(data)
            result = self.run(parsed)
            if isinstance(result, dict) and "sensor" in result and "value" in result:
                sensor = str(result["sensor"])
                value = result["value"]
                unit = str(result.get("unit", ""))
                return f"Processed {sensor} reading: {value}{unit}"
            return json.dumps(result, ensure_ascii=False)
        except Exception as exc:
            self.recover()
            raise ValueError(f"JSONAdapter failure: {exc}") from exc


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV headers or CSV rows."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, str):
                raise ValueError("CSVAdapter expects a CSV string.")
            text = data.strip().strip('"')
            if not text:
                raise ValueError("CSV input cannot be empty.")
            parts = [p.strip() for p in text.split(",") if p.strip()]
            structured = {"columns": parts, "count": len(parts)}
            result = self.run(structured)
            cols = result.get("columns", []) if isinstance(result, dict) else []
            return f"User activity logged: {len(cols)} actions processed"
        except Exception as exc:
            self.recover()
            raise ValueError(f"CSVAdapter failure: {exc}") from exc


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for real-time sensor stream summaries."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if isinstance(data, str):
                normalized = {"stream": data.strip()}
            elif isinstance(data, list):
                normalized = {"stream": "batch", "items": list(data)}
            else:
                raise ValueError("StreamAdapter expects a string or list.")
            result = self.run(normalized)
            if isinstance(result, dict) and "items" in result:
                items = result["items"]
                size = len(items) if isinstance(items, list) else 0
                return f"Stream summary: {size} readings processed"
            return result
        except Exception as exc:
            self.recover()
            raise ValueError(f"StreamAdapter failure: {exc}") from exc


class NexusManager:
    """Orchestrates multiple pipelines polymorphically and supports chaining."""

    def __init__(self, capacity_per_s: int = 1000) -> None:
        self.capacity_per_s = capacity_per_s
        self._pipelines: Dict[str, ProcessingPipeline] = {}

    def register(self, name: str, pipeline: ProcessingPipeline) -> None:
        self._pipelines[name] = pipeline

    def chain(self, pipeline_names: List[str], data: Any) -> Any:
        current = data
        for name in pipeline_names:
            pipeline = self._pipelines.get(name)
            if pipeline is None:
                raise ValueError(f"Unknown pipeline: {name}")
            current = pipeline.process(current)
        return current

    def process_queue(
        self,
        name: str,
        queue: Deque[Any],
    ) -> List[Union[str, Any]]:
        pipeline = self._pipelines.get(name)
        if pipeline is None:
            raise ValueError(f"Unknown pipeline: {name}")
        results: list[Union[str, Any]] = []
        while queue:
            item = queue.popleft()
            results.append(pipeline.process(item))
        return results


def _build_default_stages() -> List[ProcessingStage]:
    return [InputStage(), TransformStage(), OutputStage()]


def _demo() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    manager = NexusManager(capacity_per_s=1000)
    print(f"Pipeline capacity: {manager.capacity_per_s} streams/second")

    stages = _build_default_stages()
    json_pipe = JSONAdapter("PIPE_JSON", stages=stages)
    csv_pipe = CSVAdapter("PIPE_CSV", stages=_build_default_stages())
    stream_pipe = StreamAdapter("PIPE_STREAM", stages=_build_default_stages())

    manager.register("A", json_pipe)
    manager.register("B", csv_pipe)
    manager.register("C", stream_pipe)

    print("\n=== Multi-Format Data Processing ===")
    json_input = '{"sensor": "temp", "value": 23.5, "unit": "°C"}'
    print("Processing JSON data through pipeline...")
    print(f"Input: {json_input}")
    print(f"Output: {json_pipe.process(json_input)}")

    csv_input = '"user,action,timestamp"'
    print("\nProcessing CSV data through same pipeline...")
    print(f"Input: {csv_input}")
    print(f"Output: {csv_pipe.process(csv_input)}")

    print("\nProcessing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print(f"Output: {stream_pipe.process(['temp:22.1', 'temp:22.2'])}")

    print("\n=== Pipeline Chaining Demo ===")
    chain_result = manager.chain(["A", "B", "C"], json_input)
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print(f"Chain result: {chain_result}")

    print("\n=== Error Recovery Test ===")
    try:
        print("Simulating pipeline failure...")
        _ = json_pipe.process("{not valid json}")
    except ValueError as exc:
        print(f"Error detected: {exc}")
        print("Recovery initiated: Switching to backup processor")
        json_pipe.recover()
        print("Recovery status:", json_pipe.get_stats())

    print("\nQueue processing demo (collections.deque):")
    q: Deque[Any] = deque([json_input, json_input])
    results = manager.process_queue("A", q)
    print(f"Processed {len(results)} items:", results)

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    _demo()
