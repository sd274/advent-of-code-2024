from argparse import ArgumentParser
from typing import Literal

from rich import print

from advent.day_1.puzzle_1 import Day1Puzzle1
from advent.day_1.puzzle_2 import Day1Puzzle2
from advent.day_2.puzzle_1 import Day2Puzzle1
from advent.day_2.puzzle_2 import Day2Puzzle2
from advent.day_3.puzzle_1 import Day3Puzzle1
from advent.day_3.puzzle_2 import Day3Puzzle2
from advent.day_4.puzzle_1 import Day4Puzzle1
from advent.day_4.puzzle_2 import Day4Puzzle2
from advent.day_5.puzzle_1 import Day5Puzzle1
from advent.day_6.puzzle_1 import Day6Puzzle1

type supportedDays = Literal[1, 2, 3, 4, 5, 6]


def main(day: supportedDays, sample: bool, puzzle: Literal[1, 2]):
    print(f"\n\nRunning puzzle {puzzle} for day {day} (sample={sample})")
    match day:
        case 1:
            match puzzle:
                case 1:
                    to_run = Day1Puzzle1()
                case 2:
                    to_run = Day1Puzzle2()
        case 2:
            match puzzle:
                case 1:
                    to_run = Day2Puzzle1()
                case 2:
                    to_run = Day2Puzzle2()
        case 3:
            match puzzle:
                case 1:
                    to_run = Day3Puzzle1()
                case 2:
                    to_run = Day3Puzzle2()
        case 4:
            match puzzle:
                case 1:
                    to_run = Day4Puzzle1()
                case 2:
                    to_run = Day4Puzzle2()
        case 5:
            match puzzle:
                case 1:
                    to_run = Day5Puzzle1()
                case 2:
                    to_run = Day5Puzzle1()
        case 6:
            match puzzle:
                case 1:
                    to_run = Day6Puzzle1()
                case 2:
                    to_run = Day6Puzzle1()
    ans = to_run.run(sample=sample)
    print(f"    - Answer: {ans:.0f}\n\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--day", dest="day", type=int)
    parser.add_argument("--puzzle", dest="puzzle", type=int)
    parser.add_argument("--sample", dest="sample", action="store_true", default=False)
    args = parser.parse_args()
    days = args.day
    puzzle = args.puzzle
    sample = args.sample
    main(days, sample, puzzle)
