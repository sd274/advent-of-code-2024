from collections import Counter
import os
from advent import PuzzleBase


class Day1Puzzle2(PuzzleBase):
    def run(self, sample: bool):
        first_list, second_list = self.get_data(sample)
        second_list_counter = Counter(second_list)
        counts = [x * second_list_counter.get(x, 0) for x in first_list]
        answer = sum(counts)
        return answer

    def get_data(self, sample: bool) -> tuple[list[int], list[int]]:
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

    def _parse_data(self, raw_data: str) -> tuple[list[int], list[int]]:
        lines = [line.split("   ") for line in raw_data.split("\n") if line]
        first = [int(x[0]) for x in lines]
        second = [int(x[1]) for x in lines]
        return first, second
