from typing import Any, Union
from scipy import stats


def checker(*args: Any, **kwargs: Any) -> Union[tuple, dict]:
    if args and kwargs:
        raise "Not allowed. Either args only or kwargs only."
    if args:
        return args
    return kwargs


def calculate_z_score(confidence_level: float) -> float:
    return stats.norm.ppf(1 - (1 - confidence_level) / 2)


def calculate_n0(z_score: float, target_proportion: float, margin_of_error: float) -> float:
    return (z_score ** 2) * target_proportion * (1 - target_proportion) / (margin_of_error ** 2)


def calculate_n(n0: float, total_population) -> float:
    return n0 / (1 + (n0 - 1) / total_population)
