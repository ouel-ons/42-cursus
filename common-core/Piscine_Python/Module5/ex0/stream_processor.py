#!/usr/bin/env python3
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

    @abstractmethod
    def _validation_message(self) -> str:
        raise NotImplementedError

    def run(self, data: Any) -> str:
        # These two lines must appear exactly like the subject example.
        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise ValueError("Invalid data for this processor")
            print(f"Validation: {self._validation_message()}")
            result = self.process(data)
            return self.format_output(result)
        except Exception as exc:
            # Required error handling (not triggered in the example run)
            return self.format_output(f"Error: {exc}")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        nums: List[float] = [float(x) for x in data]  # type: ignore[arg-type]
        total = sum(nums)
        avg = total / len(nums)
        return f"Processed {len(nums)} numeric values, sum={int(total)}, avg={avg:.1f}"

    def _validation_message(self) -> str:
        return "Numeric data verified"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        text: str = data  # type: ignore[assignment]
        char_count = len(text)
        word_count = len(text.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def _validation_message(self) -> str:
        return "Text data verified"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and (data.startswith("ERROR:") or data.startswith("INFO:"))

    def process(self, data: Any) -> str:
        entry: str = data  # type: ignore[assignment]
        level, _, msg = entry.partition(":")
        msg = msg.strip()
        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {msg}"
        return f"[INFO] INFO level detected: {msg}"

    def _validation_message(self) -> str:
        return "Log entry verified"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    out1 = NumericProcessor().run([1, 2, 3, 4, 5])
    print(out1)

    print("Initializing Text Processor...")
    out2 = TextProcessor().run("Hello Nexus World")
    print(out2)

    print("Initializing Log Processor...")
    out3 = LogProcessor().run("ERROR: Connection timeout")
    print(out3)

    print("=== Polymorphic Processing Demo ===")
    print()  # blank line exactly like the example

    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_items: list[Any] = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]

    results: list[str] = []
    for proc, item in zip(processors, data_items, strict=True):
        try:
            if not proc.validate(item):
                raise ValueError("Invalid data")
            results.append(proc.process(item))
        except Exception as exc:
            results.append(f"Error: {exc}")

    print(f"Result 1: {results[0]}")
    print(f"Result 2: {results[1]}")
    print(f"Result 3: {results[2]}")
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
