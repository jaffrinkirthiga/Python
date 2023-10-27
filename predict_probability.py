import sys
from itertools import product


def predict_probability(days):
    absent = "0"
    present = "1"
    attendance_elements = [absent, present]
    invalid_attendance = absent * 4

    total_combinations = [
        ''.join(combination) for combination in product(
            attendance_elements,
            repeat=days
        )
    ]
    failure_combinations = list(filter(
        lambda x: invalid_attendance in x,
        total_combinations
    ))
    success_combinations = set(total_combinations) - set(failure_combinations)

    no_ways_to_attend_classes = len(total_combinations) - len(failure_combinations)

    probability_not_attend_graduation = list(filter(
        lambda x: x.startswith(absent),
        success_combinations)
    )

    return f"{len(probability_not_attend_graduation)} / {no_ways_to_attend_classes}"


if __name__ == "__main__":
    num_days = int(sys.argv[1])
    result = predict_probability(num_days)
    print(result)
