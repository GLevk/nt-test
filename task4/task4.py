import sys

LIMIT_MESSAGE = "20 ходов недостаточно для приведения всех элементов массива к одному числу"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python task4.py nums_file")

    nums_file = sys.argv[1]
    nums = []
    with open(nums_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                nums.append(int(line))

    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(x - median) for x in nums)

    if moves <= 20:
        print(moves)
    else:
        print(LIMIT_MESSAGE)


if __name__ == "__main__":
    main()
