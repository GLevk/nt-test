import sys


def build_path(n: int, m: int) -> str:
    result = []
    current = 1
    while True:
        result.append(str(current))
        current = ((current - 1 + (m - 1)) % n) + 1
        if current == 1:
            break
    return "".join(result)


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit("Usage: python task1.py n1 m1 n2 m2")

    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])

    print(build_path(n1, m1) + build_path(n2, m2))


if __name__ == "__main__":
    main()
