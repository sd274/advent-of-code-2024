import os
from advent import PuzzleBase


class Day4Puzzle2(PuzzleBase):
    def run(self, sample: bool) -> int:
        data = self.get_data(sample)
        word_to_match = "mas"
        starting_locs = [
            (i, j)
            for i, line in enumerate(data)
            for j, ch in enumerate(line)
            if ch == word_to_match[1]
        ]
        matches = [
            self._check_xmas(starting_loc, data) for starting_loc in starting_locs
        ]
        return sum(matches)

    def _check_xmas(self, starting_loc: tuple[int, int], data: list[list[str]]) -> bool:
        up_right = self._extract_up_right(starting_loc, data)
        up_left = self._extract_up_left(starting_loc, data)
        down_right = self._extract_down_right(starting_loc, data)
        down_left = self._extract_down_left(starting_loc, data)
        if up_right == down_left:
            return False
        if up_left == down_right:
            return False
        correct_letters = all(
            ch in ["m", "s"] for ch in (up_right, up_left, down_right, down_left)
        )
        return correct_letters

    def _extract_up_right(
        self, starting_loc: tuple[int, int], data: list[list[str]]
    ) -> str | None:
        x_idx = starting_loc[0] - 1
        y_idx = starting_loc[1] + 1
        if x_idx < 0 or y_idx >= len(data[0]):
            return None
        return data[x_idx][y_idx]

    def _extract_up_left(
        self, starting_loc: tuple[int, int], data: list[list[str]]
    ) -> str | None:
        x_idx = starting_loc[0] - 1
        y_idx = starting_loc[1] - 1
        if x_idx < 0 or y_idx < 0:
            return None
        return data[x_idx][y_idx]

    def _extract_down_right(
        self, starting_loc: tuple[int, int], data: list[list[str]]
    ) -> str | None:
        x_idx = starting_loc[0] + 1
        y_idx = starting_loc[1] + 1
        if x_idx >= len(data) or y_idx >= len(data[0]):
            return None
        return data[x_idx][y_idx]

    def _extract_down_left(
        self, starting_loc: tuple[int, int], data: list[list[str]]
    ) -> str | None:
        x_idx = starting_loc[0] + 1
        y_idx = starting_loc[1] - 1
        if x_idx >= len(data) or y_idx < 0:
            return None
        return data[x_idx][y_idx]

    def get_data(self, sample: bool) -> list[list[str]]:
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

    def _parse_data(self, raw_data: str):
        return [[ch.lower() for ch in line] for line in raw_data.split("\n") if line]
