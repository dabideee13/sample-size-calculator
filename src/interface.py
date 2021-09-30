from abc import ABC, abstractmethod
from typing import Any


class IPrompter(ABC):
    @abstractmethod
    def prompt(self) -> None:
        raise NotImplementedError


class IParameter(ABC):
    @property
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def values(self) -> None:
        raise NotImplementedError


class ICalculator(ABC):
    @abstractmethod
    def calculate(self, **kwargs: Any) -> None:
        raise NotImplementedError
