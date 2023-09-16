import argparse
import json
from jsonpath_ng import parse


def parse_json(file: str, json_path: str) -> None:
    with open(file, 'r') as f:
        json_data = json.load(f)

    jsonpath_expr = parse(json_path)

    matches = [match.value for match in jsonpath_expr.find(json_data)]
    print(matches)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path for your JSON file.",
    )
    parser.add_argument(
        "--json_path",
        type=str,
        required=True,
        help="Your JSONPath expression."
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    parse_json(file=args.file, json_path=args.json_path)
