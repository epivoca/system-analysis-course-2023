import argparse
import numpy as np


def task(matrix_csv: str):
    matrix = []
    lines = matrix_csv.split("\n")
    for line in lines:
        matrix.append(list(map(int, line.split(","))))

    n = len(matrix)
    H = 0
    for row in matrix:
        for num in row:
            p = num / (n-1)
            if p > 0:
                H -= p * np.log2(p)

    return H


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--csv_content",
        type=str,
        required=True,
        help="Row with csv-like data.",
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    result2 = t2("1,2\n2,3\n2,6\n3,4\n3,5")
    result3 = task(result2)
    print(result3)