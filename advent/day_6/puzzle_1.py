import os
from dataclasses import dataclass
from typing import Literal
from advent import PuzzleBase


@dataclass
class CurrentGuardPosition:
    x: int
    y: int
    direction: Literal[0, 1, 2, 3]


@dataclass
class Grid:
    width: int
    height: int
    obstruction_locations: list[tuple[int, int]]

    def __str__(self) -> str:
        to_print = ""
        for y in range(self.height):
            line_to_print = ""
            for x in range(self.width):
                if (x, y) in self.obstruction_locations:
                    line_to_print += "#"
                else:
                    line_to_print += "."
            to_print += f"{line_to_print}\n"
        return to_print

    def print_with_guard(self, guard_loc: CurrentGuardPosition) -> str:
        to_print = ""
        for y in range(self.height):
            line_to_print = ""
            for x in range(self.width):
                if (x, y) == (guard_loc.x, guard_loc.y):
                    line_to_print += "*"
                elif (x, y) in self.obstruction_locations:
                    line_to_print += "#"
                else:
                    line_to_print += "."
            to_print += f"{line_to_print}\n"
        return to_print


class Day6Puzzle1(PuzzleBase):
    def run(self, sample: bool) -> int:
        grid, guard_loc = self.get_data(sample)
        guard_locs: list[tuple[int, int]] = []
        while self._check_on_grid(grid, guard_loc):
            guard_locs.append((guard_loc.x, guard_loc.y))
            dx, dy, d_dir = self._choose_next_move(grid, guard_loc)
            guard_loc = CurrentGuardPosition(
                x=guard_loc.x + dx,
                y=guard_loc.y + dy,
                direction=(guard_loc.direction + d_dir) % 4,
            )
        ans = len(set(guard_locs))

        return ans

    def _choose_next_move(
        self, grid: Grid, guard_loc: CurrentGuardPosition
    ) -> tuple[int, int, int]:
        current_dir = guard_loc.direction
        match current_dir:
            case 0:
                potential_next = (guard_loc.x, guard_loc.y - 1)
                if potential_next in grid.obstruction_locations:
                    return 0, 0, 1
                return 0, -1, 0
            case 1:
                potential_next = (guard_loc.x + 1, guard_loc.y + 0)
                if potential_next in grid.obstruction_locations:
                    return 0, 0, 1
                return 1, 0, 0
            case 2:
                potential_next = (guard_loc.x + 0, guard_loc.y + 1)
                if potential_next in grid.obstruction_locations:
                    return 0, 0, 1
                return 0, 1, 0
            case 3:
                potential_next = (guard_loc.x - 1, guard_loc.y)
                if potential_next in grid.obstruction_locations:
                    return 0, 0, 1
                return -1, 0, 0

    def _check_on_grid(self, grid: Grid, loc: CurrentGuardPosition) -> bool:
        if loc.x > grid.width:
            return False
        if loc.x < 0:
            return False
        if loc.y > grid.height:
            return False
        if loc.y < 0:
            return False
        return True

    def get_data(self, sample: bool):
        raw = self._get_raw(sample)
        return self._parse_data(raw)

    def _get_raw(self, sample: bool) -> str:
        match sample:
            case True:
                filepath = os.path.join(os.path.dirname(__file__), "sample_input.txt")
            case False:
                filepath = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(filepath, "r") as file:
            raw_data = file.read()
        return raw_data

    def _parse_data(self, raw: str):
        lines_raw = raw.split("\n")
        lines = [[ch for ch in line] for line in lines_raw if line]
        assert max(len(line) for line in lines) == min(len(line) for line in lines)
        width = max(len(line) for line in lines)
        height = len(lines)
        obstruction_locations = [
            (x_idx, y_idx)
            for y_idx, line in enumerate(lines)
            for x_idx, ch in enumerate(line)
            if ch == "#"
        ]
        direction_map: dict[
            str,
            Literal[
                0,
                1,
                2,
                3,
            ],
        ] = {"^": 0, ">": 1, "<": 3, "v": 2}
        current_guard_vector = next(
            (x_idx, y_idx, direction_map.get(ch))
            for y_idx, line in enumerate(lines)
            for x_idx, ch in enumerate(line)
            if ch in direction_map.keys()
        )

        return Grid(
            width=width,
            height=height,
            obstruction_locations=obstruction_locations,
        ), CurrentGuardPosition(
            current_guard_vector[0], current_guard_vector[1], current_guard_vector[2]
        )
