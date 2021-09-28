from math import ceil

from scipy import stats


def calculate_z_score(confidence_level: float) -> float:
    return stats.norm.ppf(1 - (1 - confidence_level) / 2)


def calculate_n0(z_score: float, target_proportion: float, margin_of_error: float) -> float:
    return (z_score ** 2) * target_proportion * (1 - target_proportion) / (margin_of_error ** 2)


def calculate_n(n0: float, total_population) -> float:
    return n0 / (1 + (n0 - 1) / total_population)


def calculate_sample_size(total_population: int, confidence_level: float, margin_of_error: float, target_proportion: float) -> int:
    z_score = get_z_score(confidence_level)
    n0 = calculate_n0(z_score, target_proportion, margin_of_error)
    return ceil(calculate_n(n0, total_population))


def main():

    calculate_sample_size(total_population=100000, confidence_level=0.95, margin_of_error=0.05, target_proportion=0.5)


if __name__ == '__main__':
    main()
