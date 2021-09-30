from typing import Optional, Any, Union
from collections import namedtuple
from abc import ABC, abstractmethod
from math import ceil

from utils import calculate_z_score, calculate_n0, calculate_n


def checker(*args: Any, **kwargs: Any) -> Union[tuple, dict]:
    if args and kwargs:
        raise "Not allowed. Either args only or kwargs only."
    if args:
        return args
    return kwargs


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


class Parameter(IParameter):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._values = checker(*args, **kwargs)

    @property
    def values(self) -> Union[tuple, dict]:
        if isinstance(self._values, tuple):
            return tuple(arg for arg in self._values)
        elif isinstance(self._values, dict):
            return {key: val for key, val in self._values.items()}
        else:
            raise TypeError(
                "Return of args and kwargs changed. Maybe there's an update with Python."
            )


class SampleSizeParameter(Parameter):
    """
    Calculates sample size following Cochran's formula, which is dependent on
    total population, confidence level, margin of error, and target proportion.

    Example:
        >>> params = SampleSizeParameter(total_population=100, confidence_level=0.95, margin_of_error=0.05, target_proportion=0.5)
        >>> print(params.values)
        Parameter(total_population=100, confidence_level=0.95, margin_of_error=0.05, target_proportion=0.5)

        >>> params = SampleSizeParameter(100, 0.95, 0.05, 0.5)
        >>> print(params.values)
        Parameter(total_population=100, confidence_level=0.95, margin_of_error=0.05, target_proportion=0.5)
    """

    Parameter = namedtuple(
        "Parameter",
        "total_population confidence_level margin_of_error target_proportion",
    )

    @property
    def values(self) -> namedtuple:

        _params = super().values

        if isinstance(_params, tuple):
            return self.Parameter(*_params)

        if tuple(_params.keys()) == tuple(self.Parameter._fields):
            return self.Parameter(*_params.values())


class SampleSizePrompter(IPrompter):
    def prompt(self) -> None:

        total_population = int(input("Total population: "))
        confidence_level = float(input("Confidence level: "))
        margin_of_error = float(input("Margin of error: "))
        target_proportion = float(input("Target proportion: "))

        return SampleSizeParameter.Parameter(
            total_population, confidence_level, margin_of_error, target_proportion
        )


class SampleSizeCalculator(ICalculator):
    def __init__(self) -> None:
        self.sample_size = None

    def calculate(
        self,
        total_population: int,
        confidence_level: float,
        margin_of_error: float,
        target_proportion: float,
    ) -> int:
        z_score = calculate_z_score(confidence_level)
        n0 = calculate_n0(z_score, target_proportion, margin_of_error)
        self.sample_size = ceil(calculate_n(n0, total_population))
        return self.sample_size


def main():

    prompt = SampleSizePrompter()
    params = SampleSizeParameter(*prompt.prompt())

    calculator = SampleSizeCalculator()
    calculator.calculate(*params.values)
    print(calculator.sample_size)


if __name__ == "__main__":
    main()
