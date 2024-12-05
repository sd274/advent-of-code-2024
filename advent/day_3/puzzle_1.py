import re
import os
from advent import PuzzleBase


class Day3Puzzle1(PuzzleBase):
    def run(self, sample: bool) -> int:
        reports = self.get_data(sample)
        match_str = r"mul\(\d+,\d+\)"
        matches = re.findall(match_str, reports) or []
        multiplications = [self._process_multi(x) for x in matches]
        answer = sum(multiplications)
        return answer

    def _process_multi(self, x: str) -> int:
        striped = x.replace("mul(", "").replace(")", "")
        split = striped.split(",")
        return int(split[0]) * int(split[1])

    def get_data(self, sample: bool) -> str:
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

    def _parse_data(self, raw_data: str) -> str:
        return raw_data
