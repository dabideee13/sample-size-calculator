from typing import Optional, Any, Union
from collections import namedtuple
from abc import ABC, abstractmethod

from tools import calculate_z_score, calculate_n0, calculate_n, checker
from core import SampleSizePrompter, SampleSizeParameter, SampleSizeCalculator


def main():

    prompt = SampleSizePrompter()
    params = SampleSizeParameter(*prompt.prompt())

    calculator = SampleSizeCalculator()
    calculator.calculate(*params.values)
    print(calculator.sample_size)


if __name__ == "__main__":
    main()
