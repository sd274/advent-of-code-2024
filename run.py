from argparse import ArgumentParser
from typing import Literal

from advent.day_1.puzzle_1 import Day1Puzzle1
from advent.day_1.puzzle_2 import Day1Puzzle2
from advent.day_2.puzzle_1 import Day2Puzzle1
from advent.day_2.puzzle_2 import Day2Puzzle2
from advent.day_3.puzzle_1 import Day3Puzzle1

type supportedDays = Literal[
    1,
    2,
    3,
    4,
]


def main(day: supportedDays, sample: bool, puzzle: Literal[1, 2]):
    match day:
        case 1:
            match puzzle:
                case 1:
                    Day1Puzzle1().run(sample=sample)
                case 2:
                    Day1Puzzle2().run(sample=sample)
        case 2:
            match puzzle:
                case 1:
                    Day2Puzzle1().run(sample=sample)
                case 2:
                    Day2Puzzle2().run(sample=sample)
        case 3:
            match puzzle:
                case 1:
                    Day3Puzzle1().run(sample=sample)
                case 2:
                    Day2Puzzle2().run(sample=sample)
        case 4:
            print("running day 1")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--day", dest="day", type=int)
    parser.add_argument("--puzzle", dest="puzzle", type=int)
    parser.add_argument("--sample", dest="sample", action="store_true", default=False)
    args = parser.parse_args()
    days = args.day
    puzzle = args.puzzle
    sample = args.sample
    print(f"Sample: {sample}")
    main(days, sample, puzzle)
