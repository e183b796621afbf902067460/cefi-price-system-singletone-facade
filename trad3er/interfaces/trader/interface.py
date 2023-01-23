from abc import ABC, abstractmethod
from typing import Optional


class iTrad3r(ABC):

    _endpoint: Optional[str] = None

    @abstractmethod
    def get_price(self, first: str, second: str, *args, **kwargs) -> float:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.get_price.__name__}() implementation")
