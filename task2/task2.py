import sys
from decimal import Decimal, getcontext

getcontext().prec = 100


def classify_point(cx: Decimal, cy: Decimal, a: Decimal, b: Decimal, x: Decimal, y: Decimal) -> int:
    value = ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2)
    one = Decimal("1")
    if value == one:
        return 0
    if value < one:
        return 1
    return 2


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python task2.py ellipse_file points_file")

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(ellipse_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    cx, cy = map(Decimal, lines[0].split())
    a, b = map(Decimal, lines[1].split())

    with open(points_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(Decimal, line.split())
            print(classify_point(cx, cy, a, b, x, y))


if __name__ == "__main__":
    main()
