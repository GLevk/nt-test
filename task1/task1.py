import sys

def get_array_path(n, m):
    path = []
    arr = [i + 1 for i in range(n)]
    current_pos = 0

    while True:
        path.append(arr[current_pos])
        current_pos = (current_pos + m - 1) % n

        if arr[current_pos] == arr[0]:
            break

    return ''.join(map(str, path))


def main():
    if len(sys.argv) != 5:
        print("Ошибка: передайте 4 аргумента: n1 m1 n2 m2")
        return

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:])
    except:
        print("Ошибка: все аргументы должны быть целыми числами")
        return

    if n1 < 1 or m1 < 1 or n2 < 1 or m2 < 1:
        print("Ошибка: все числа должны быть больше 0")
        return

    first_path = get_array_path(n1, m1)
    second_path = get_array_path(n2, m2)

    print(first_path + second_path)


if __name__ == "__main__":
    main()
