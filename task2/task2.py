import sys


def check_point(center, radius, x, y):
    center_x, center_y = center
    radius_x, radius_y = radius

    value = ((x - center_x) ** 2) / (radius_x ** 2) + ((y - center_y) ** 2) / (radius_y ** 2)

    if abs(value - 1) < 1e-12:
        return 0
    elif value < 1:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Ошибка: нужно передать 2 файла: ellipse_file points_file")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        with open(ellipse_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Ошибка: файл с эллипсом не найден")
        return

    if len(lines) != 2:
        print("Ошибка: файл с эллипсом должен содержать 2 строки")
        return

    try:
        center = list(map(float, lines[0].split()))
        radius = list(map(float, lines[1].split()))
    except ValueError:
        print("Ошибка: в файле эллипса должны быть числа")
        return

    if len(center) != 2 or len(radius) != 2:
        print("Ошибка: в каждой строке файла эллипса должно быть по 2 числа")
        return

    if radius[0] <= 0 or radius[1] <= 0:
        print("Ошибка: полуоси эллипса должны быть больше 0")
        return

    try:
        with open(points_file, "r", encoding="utf-8") as f:
            points_lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Ошибка: файл с точками не найден")
        return

    if len(points_lines) == 0:
        print("Ошибка: файл с точками пустой")
        return

    points = []

    for line in points_lines:
        try:
            point = list(map(float, line.split()))
        except ValueError:
            print("Ошибка: в файле точек должны быть только числа")
            return

        if len(point) != 2:
            print("Ошибка: каждая точка должна содержать 2 числа")
            return

        points.append(point)

    for point in points:
        result = check_point(center, radius, point[0], point[1])
        print(result)


if __name__ == "__main__":
    main()

