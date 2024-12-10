from collections import defaultdict
import os
from typing import dataclass_transform
from advent import PuzzleBase

type UpdateRule = defaultdict[int, list[int]]
type Update = list[int]


class Day5Puzzle1(PuzzleBase):
    def run(self, sample: bool) -> int:
        update_map, updates = self.get_data(sample)
        correct_updates = [
            update for update in updates if self._check_update(update, update_map)
        ]
        print(correct_updates)
        middle_values = [self._extract_middle(update) for update in correct_updates]

        return sum(middle_values)

    def _extract_middle(self, update: Update) -> int:
        update_len = len(update)
        assert update_len % 2 == 1, update
        middle = (update_len - 1) // 2
        return update[middle]

    def _check_update(self, update: Update, update_map: UpdateRule) -> bool:
        for index, el in enumerate(update):
            update_values = update_map.get(el)
            if update_values is None:
                pass
            else:
                for update_value in update_values:
                    if update_value in update[:index]:
                        return False
        return True

    def get_data(self, sample: bool) -> tuple[UpdateRule, list[Update]]:
        raw_data = self._load_data(sample)
        return self._parse_data(raw_data)

    def _load_data(self, sample: bool) -> str:
        if sample:
            filepath = os.path.join(os.path.dirname(__file__), "sample_input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()

        else:
            filepath = os.path.join(os.path.dirname(__file__), "input.txt")
            with open(filepath, "r") as file:
                raw_data = file.read()
        return raw_data

    def _parse_data(self, raw_data: str) -> tuple[UpdateRule, list[Update]]:
        split = raw_data.split("\n\n")

        rules_raw = split[0]
        rules_tuples = [x.split("|") for x in rules_raw.split("\n") if x]
        rules_map: UpdateRule = defaultdict(list[int])
        for rule_tuple in rules_tuples:
            rules_map[int(rule_tuple[0])].append(int(rule_tuple[1]))


        updates = split[1].split("\n")
        updates = [
            [int(el) for el in line.split(",") if el != ""] for line in updates if line
        ]
        return rules_map, updates
