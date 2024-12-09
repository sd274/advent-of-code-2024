import os
from advent import PuzzleBase


class Day4Puzzle1(PuzzleBase):
    def run(self, sample: bool) -> int:
        data = self.get_data(sample)
        print(f" : {' '.join(str(i) for i in range(len(data[0])))}")
        for lin_num, line in enumerate(data):
            print(f"{lin_num:,.0f}: {' '.join(x for x in line)}")
        word_to_match = "xmas"
        starting_locs = [
            (i, j)
            for i, line in enumerate(data)
            for j, ch in enumerate(line)
            if ch == word_to_match[0]
        ]
        matches = [
            self._count_matches(starting_loc, data, word_to_match)
            for starting_loc in starting_locs
        ]
        return sum(matches)

    def _count_matches(
        self, starting_loc: tuple[int, int], data: list[list[str]], word_to_match: str
    ) -> int:
        print(starting_loc)
        word_len = len(word_to_match)
        right_word = self._extract_right_word(starting_loc, data, word_len)
        total = 0
        if right_word == word_to_match:
            total += 1
        left_word = self._extract_left_word(starting_loc, data, word_len)
        if left_word == word_to_match:
            total += 1
        down_word = self._extract_down_word(starting_loc, data, word_len)
        if down_word == word_to_match:
            total += 1
        up_word = self._extract_up_word(starting_loc, data, word_len)
        print(f"up word: {up_word}")
        if up_word == word_to_match:
            total += 1
        print(total)
        print("---" * 19)

        return total

    def _extract_up_word(
        self, starting_loc: tuple[int, int], data: list[list[str]], word_len: int
    ) -> str:
        return "".join(
            data[starting_loc[0] - word_len + i][starting_loc[1]]
            for i in range(word_len + 1)
            if (
                starting_loc[0] + i - word_len >= 0
                and starting_loc[0] + i - word_len + 1 < len(data[0])
            )
        )

    def _extract_down_word(
        self, starting_loc: tuple[int, int], data: list[list[str]], word_len: int
    ) -> str:
        return "".join(
            data[starting_loc[0] + i][starting_loc[1]]
            for i in range(word_len)
            if starting_loc[0] + i < len(data)
        )

    def _extract_right_word(
        self, starting_loc: tuple[int, int], data: list[list[str]], word_len: int
    ) -> str:
        line = data[starting_loc[0]]
        return "".join(line[starting_loc[1] : starting_loc[1] + word_len])

    def _extract_left_word(
        self, starting_loc: tuple[int, int], data: list[list[str]], word_len: int
    ) -> str:
        line = data[starting_loc[0]]
        characters = line[max(0, starting_loc[0] - word_len) : starting_loc[0]]
        return "".join(characters)

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
