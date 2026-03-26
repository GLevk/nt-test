import json
import sys


def fill_values(data, values_dict):
    if isinstance(data, dict):
        if "id" in data and "value" in data:
            data["value"] = values_dict.get(data["id"], data["value"])

        if "values" in data:
            for item in data["values"]:
                fill_values(item, values_dict)

    elif isinstance(data, list):
        for item in data:
            fill_values(item, values_dict)


def main():
    if len(sys.argv) != 4:
        print("Ошибка: нужно передать 3 файла: values.json tests.json report.json")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        with open(values_file, "r", encoding="utf-8") as f:
            values_data = json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл values.json не найден")
        return
    except json.JSONDecodeError:
        print("Ошибка: файл values.json содержит некорректный JSON")
        return

    try:
        with open(tests_file, "r", encoding="utf-8") as f:
            tests_data = json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл tests.json не найден")
        return
    except json.JSONDecodeError:
        print("Ошибка: файл tests.json содержит некорректный JSON")
        return

    if "values" not in values_data or not isinstance(values_data["values"], list):
        print("Ошибка: в values.json должен быть список values")
        return

    if "tests" not in tests_data or not isinstance(tests_data["tests"], list):
        print("Ошибка: в tests.json должен быть список tests")
        return

    values_dict = {}

    for item in values_data["values"]:
        if "id" in item and "value" in item:
            values_dict[item["id"]] = item["value"]

    fill_values(tests_data["tests"], values_dict)

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(tests_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
