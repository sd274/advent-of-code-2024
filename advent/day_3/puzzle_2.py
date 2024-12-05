import re
import os
from typing import TypedDict
from advent import PuzzleBase


class CommandIndex(TypedDict):
    command: str
    start: int
    end: int | None


class Day3Puzzle2(PuzzleBase):
    def run(self, sample: bool):
        reports = self.get_data(sample)
        match_str = r"mul\(\d+,\d+\)"
        matches = re.finditer(match_str, reports) or []
        do_matches = re.finditer(r"do\(\)", reports) or []
        dont_matches = re.finditer(r"don't\(\)", reports) or []
        do_indexs = [0] + [m.end() for m in do_matches]
        dont_indexs = [m.end() for m in dont_matches]
        index_map: list[tuple[int, str]] = sorted(
            [(x, "do") for x in do_indexs] + [(x, "dont") for x in dont_indexs],
            key=lambda x: x[0],
        )
        rules: list[CommandIndex] = []
        for i in range(len(index_map) - 1):
            rules.append(
                {
                    "command": index_map[i][1],
                    "start": index_map[i][0],
                    "end": index_map[i + 1][0],
                }
            )
        rules.append(
            {"command": index_map[-1][1], "start": index_map[-1][0], "end": None}
        )

        multiplications = [
            self._process_multi(x.group(0))
            for x in matches
            if self._check_do_dont(x.start(), rules)
        ]
        answer = sum(multiplications)
        return answer

    def _check_do_dont(self, start: int, rules: list[CommandIndex]):
        command = next(
            (
                rule
                for rule in rules
                if start >= rule["start"]
                and (True if rule["end"] is None else start < rule["end"])
            ),
            "do",
        )
        if command['command'] == 'do':
            return True
        return False

    def _process_multi(self, x: str) -> int:
        striped = x.replace("mul(", "").replace(")", "")
        split = striped.split(",")
        return int(split[0]) * int(split[1])

    def get_data(self, sample: bool) -> str:
        raw_data = self._load_data(sample)
        return self._parse_data(raw_data)

    def _load_data(self, sample: bool):
        if sample:
            filepath = os.path.join(os.path.dirname(__file__), "sample_2_input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()
        else:
            filepath = os.path.join(os.path.dirname(__file__), "input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()
        return raw_data

    def _parse_data(self, raw_data: str) -> str:
        return raw_data
