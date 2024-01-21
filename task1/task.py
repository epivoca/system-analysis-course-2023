import argparse
import csv
import sys

path = str(sys.argv[1])
lineIdx = int(sys.argv[2])
columnIdx = int(sys.argv[3])


def get_line(table, line_idx):
    i = 0
    line = table.readline()
    while i < line_idx:
        line = table.readline()
        i += 1
    if line is not None:
        split_line = line.split(",")
    else:
        split_line = None
    return split_line


def get_cell(split_line, column_idx):
    if len(split_line) > column_idx:
        value = split_line[columnIdx]
    else:
        value = None
    return value


def task() -> None:
    if columnIdx >= 0 and lineIdx >= 0:
        data = open(path, "r")
        cells = get_line(data, lineIdx)
        result = get_cell(cells, columnIdx)
    else:
        result = None

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
    print(task())
