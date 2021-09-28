from math import ceil

from scipy import stats


def calculate_z_score(confidence_level: float) -> float:
    return stats.norm.ppf(1 - (1 - confidence_level) / 2)


def calculate_n0(z_score: float, target_proportion: float, margin_of_error: float) -> float:
    return (z_score ** 2) * target_proportion * (1 - target_proportion) / (margin_of_error ** 2)


def calculate_n(n0: float, total_population) -> float:
    return n0 / (1 + (n0 - 1) / total_population)


def calculate_sample_size(total_population: int, confidence_level: float, margin_of_error: float, target_proportion: float) -> int:
    z_score = calculate_z_score(confidence_level)
    n0 = calculate_n0(z_score, target_proportion, margin_of_error)
    return ceil(calculate_n(n0, total_population))


def main():
    total_population = int(input('Total population: '))
    confidence_level = float(input('Confidence level: '))
    margin_of_error = float(input('Margin of error: '))
    target_proportion = float(input('Target proportion: '))

    print(f'calculated sample = {calculate_sample_size(total_population, confidence_level, margin_of_error, target_proportion)}')

    
if __name__ == '__main__':
    main()
