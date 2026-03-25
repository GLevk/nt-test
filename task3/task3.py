import json
import sys
from typing import Any, Dict


def fill_values(node: Dict[str, Any], values_map: Dict[int, str]) -> None:
    node_id = node.get("id")
    if node_id in values_map:
        node["value"] = values_map[node_id]

    for child in node.get("values", []):
        fill_values(child, values_map)


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: python task3.py values.json tests.json report.json")

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    with open(values_file, "r", encoding="utf-8") as f:
        values_data = json.load(f)

    with open(tests_file, "r", encoding="utf-8") as f:
        tests_data = json.load(f)

    values_map = {item["id"]: item["value"] for item in values_data.get("values", [])}

    for test in tests_data.get("tests", []):
        fill_values(test, values_map)

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
