import sys


def count_moves(target, numbers):
    total = 0
    for number in numbers:
        total += abs(number - target)
    return total


def find_min_moves(numbers):
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)

    median = numbers_sorted[n // 2]
    moves = count_moves(median, numbers)

    return moves


def main():
    if len(sys.argv) != 2:
        print("Ошибка: укажите файл с числами")
        return

    numbers_file = sys.argv[1]
    numbers = []

    try:
        with open(numbers_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                for x in line.split():
                    try:
                        numbers.append(int(x))
                    except ValueError:
                        print("Ошибка: в файле должны быть только целые числа")
                        return
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return

    if len(numbers) == 0:
        print("Ошибка: файл пустой")
        return

    result = find_min_moves(numbers)

    if result <= 20:
        print(result)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


if __name__ == "__main__":
    main()
