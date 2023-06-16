from abc import ABC, abstractmethod
from pyliftover import LiftOver
from typing import Tuple


class AbstractLifter(ABC):
    """Abstract class for lifters."""

    def __init__(self, from_ga: str, to_ga: str):
        """Initializes the lifter."""
        self.lo = LiftOver(from_ga, to_ga)

    def convert(
        self, chromosome: str, start: int, end: int
    ) -> Tuple[str, str, str] | None:
        """
        Converts a genomic position from one genome build to another.
        """

        print("Converting", chromosome, start, end)

        lifted_start = self.lo.convert_coordinate(chromosome, start)
        lifted_end = self.lo.convert_coordinate(chromosome, end)

        if lifted_start is None or lifted_end is None:
            return None

        if len(lifted_start) == 0 or len(lifted_end) == 0:
            return None

        return (lifted_start[0][0], str(lifted_start[0][1]), str(lifted_end[0][1]))

    @abstractmethod
    def lift(self, data: str) -> str:
        """Lifts the data."""
        raise NotImplementedError


class AbstractRowWiseLifter(AbstractLifter):
    """Abstract class for row-wise lifters."""

    def lift(self, data: str) -> str:
        """Lifts the data."""
        result = []

        for row in data.split("\n"):
            if row == "" or row.startswith("#"):
                continue

            lifted_row = self.__lift_row__(row)

            if lifted_row is None:
                continue

            result.append(lifted_row)

        return "\n".join(result)

    @abstractmethod
    def __lift_row__(self, row: str) -> str | None:
        """Lifts a single row."""
        raise NotImplementedError
