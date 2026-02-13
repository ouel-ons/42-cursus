from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class defining a common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return a result string."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if data is valid for this processor."""
        raise NotImplementedError

    def format_output(self, result: str) -> str:
        """Default output formatting (subclasses may override)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric sequences."""

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)):
            return False
        if not data:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("NumericProcessor expects a non-empty list/tuple "
                             "of int/float values.")
        values = list(data)
        total = float(sum(values))
        avg = total / len(values)
        return (
            f"Processed {len(values)} numeric values, "
            f"sum={int(total) if total.is_integer() else total}, "
            f"avg={avg}"
        )


class TextProcessor(DataProcessor):
    """Processor specialized for text."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("TextProcessor expects a string.")
        text = data.strip()
        words = [w for w in text.split() if w]
        return (
            f"Processed text: {len(text)} characters, {len(words)} words"
        )


class LogProcessor(DataProcessor):
    """Processor specialized for log entries formatted like 'LEVEL: message'."""

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("LogProcessor expects a string containing ':'.")
        level_raw, message_raw = data.split(":", 1)
        level = level_raw.strip().upper()
        message = message_raw.strip()
        if not message:
            raise ValueError("LogProcessor log message cannot be empty.")
        return f"{level} level detected: {message}"

    def format_output(self, result: str) -> str:
        # Specialized formatting to highlight alerts.
        upper = result.upper()
        prefix = "[INFO]"
        if upper.startswith("ERROR"):
            prefix = "[ALERT]"
        elif upper.startswith("WARN"):
            prefix = "[WARN]"
        return f"Output: {prefix} {result}"


def _demo() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    samples: list[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]

    for proc, sample in zip(processors, samples, strict=True):
        print(f"\nInitializing {proc.__class__.__name__}...")
        print(f"Processing data: {sample!r}")
        try:
            if proc.validate(sample):
                print("Validation: Data verified")
            else:
                print("Validation: Failed")
            result = proc.process(sample)
            print(proc.format_output(result))
        except ValueError as exc:
            print(f"Output: [ERROR] {exc}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for idx, (proc, sample) in enumerate(zip(processors, samples, strict=True), 1):
        try:
            print(f"Result {idx}: {proc.process(sample)}")
        except ValueError as exc:
            print(f"Result {idx}: [ERROR] {exc}")


if __name__ == "__main__":
    _demo()
