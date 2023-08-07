from abc import ABC, abstractmethod
from .pyliftover.pyliftover import LiftOver
from typing import Tuple
import requests


class AbstractLifter(ABC):
    """Abstract class for lifters."""

    def __init__(self, from_ga: str, to_ga: str):
        """Initializes the lifter."""
        self.lo = LiftOver(from_ga, to_ga)

    def convert_coordinate(self, chromosome: str, position: int) -> "Tuple[str, int] | None":
        lifted = self.lo.convert_coordinate(chromosome, position)
        
        if lifted is None:
            return None
        
        if len(lifted) == 0:
            return None
        
        return lifted[0][0], lifted[0][1]

    def convert_region(
        self, chromosome: str, start: int, end: int
    ) -> "Tuple[str, int, int] | None":
        """
        Converts a genomic position from one genome build to another.
        """

        lifted_start = self.convert_coordinate(chromosome, start)
        lifted_end = self.convert_coordinate(chromosome, end)

        if lifted_start is None or lifted_end is None:
            print(f"Could not lift {chromosome}:{start}-{end}")
            return None

        return (lifted_start[0], lifted_start[1], lifted_end[1])

    @abstractmethod
    def lift_path(self, path: str) -> str:
        """Lifts a path."""
        raise NotImplementedError

    @abstractmethod
    def lift_url(self, url: str) -> str:
        """Lifts a URL."""
        raise NotImplementedError
    
class AbstractTextLifter(AbstractLifter):
    """Abstract class for lifters of text-based files."""
    
    @abstractmethod
    def lift_content(self, content: str) -> str:
        """Lifts the content of a file."""
        raise NotImplementedError
    
    def lift_path(self, path: str) -> str:
        """Lifts a path."""
        with open(path) as f:
            content = f.read()
        
        return self.lift_content(content)
    
    def lift_url(self, url: str) -> str:
        """Lifts a URL."""
        response = requests.get(url)
        
        return self.lift_content(response.text)


class AbstractRowWiseTextLifter(AbstractTextLifter):
    """Abstract class for row-wise lifters."""

    def lift_content(self, content: str) -> str:
        """Lifts the content."""
        result = []

        for row in content.split("\n"):
            if row == "" or row.startswith("#"):
                continue

            lifted_row = self.__lift_row__(row)

            if lifted_row is None:
                continue

            result.append(lifted_row)

        return "\n".join(result)

    @abstractmethod
    def __lift_row__(self, row: str) -> "str | None":
        """Lifts a single row."""
        raise NotImplementedError
