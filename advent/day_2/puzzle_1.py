import os
from advent import PuzzleBase


class Day2Puzzle1(PuzzleBase):
    def run(self, sample: bool):
        reports = self.get_data(sample)
        safe_reports = [self._is_safe(line) for line in reports]
        answer = sum(safe_reports)
        print(f"Answer: {answer:.0f}")

    def _is_safe(self, line: list[int]) -> bool:
        first_difference = line[0] < line[1]
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                return False
            difference = line[i] < line[i + 1]
            if first_difference != difference:
                return False
            if abs(line[i] - line[i + 1]) > 3:
                return False
        return True

    def get_data(self, sample: bool) -> list[list[int]]:
        raw_data = self._load_data(sample)
        return self._parse_data(raw_data)

    def _load_data(self, sample: bool):
        if sample:
            filepath = os.path.join(os.path.dirname(__file__), "sample_input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()

        else:
            filepath = os.path.join(os.path.dirname(__file__), "input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()
        return raw_data

    def _parse_data(self, raw_data: str) -> list[list[int]]:
        lines = raw_data.split("\n")
        reports = [line.split(" ") for line in lines if line]
        return [[int(x) for x in line] for line in reports if line]
