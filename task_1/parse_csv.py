import argparse
import csv


def parse_csv(file: str, x: int, y: int) -> None:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        csv_data = list(csv_reader)

    print(csv_data[x][y])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path for your CSV file.",
    )
    parser.add_argument(
        "--x",
        type=str,
        required=True,
        help="Row index."
    )
    parser.add_argument(
        "--y",
        type=str,
        required=True,
        help="Column index."
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    parse_csv(file=args.file, x=args.x, y=args.y)
