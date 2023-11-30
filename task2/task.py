import argparse


def display_graph(edges_csv: str) -> None:
    edges = edges_csv.split('\n')
    matrix = []

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1
        while sup > len(matrix) - 1 or inf > len(matrix) - 1:
            matrix.append([0, 0, 0, 0, 0])

        matrix[sup][0] += 1
        matrix[inf][1] += 1

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1
        matrix[sup][2] += matrix[inf][0]
        matrix[inf][3] += matrix[sup][1]
        matrix[inf][4] += matrix[sup][0] - 1

    result = ""
    for row in matrix:
        for col in row:
            result += str(col)+","

        result = result[:-1]+"\n"

    print(result[:-1])


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
    display_graph(edges_csv=args.csv_content)
