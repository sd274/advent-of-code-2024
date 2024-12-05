from abc import ABC, abstractmethod


class PuzzleBase(ABC):
    @abstractmethod
    def run(self, sample: bool) -> int:
        pass
