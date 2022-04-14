from geometry_classe import GeometryFigure


def print_menu():
    print("1 - Посмотреть информацию о фигурах")
    print("2 - Сдвинуть треугольник")
    print("3 - Сдвинуть четырёхугольник")
    print("4 - Сравнить площади фигур")


def input_category():
    print("Выберите категорию")

    while True:
        try:
            x = int(input())

            if x in range(1, 5):
                return x
            print("Введите одно целое число от 1 до 4")

        except ValueError:
            print("Введите целое число")


def input_point():
    while True:
        try:
            x, y = map(float, input().split())
            return {"x": x, "y": y}
        except ValueError:
            print("Невверно введены вершины")


def create_figure(count_side, name_figure) -> GeometryFigure:
    print(f"Введите вершины фигуры {name_figure}. Ввод осуществляется по одной вершине")
    print("Координаты вводите через пробел: x y")

    while True:
        points = []
        for _ in range(count_side):
            points += [input_point()]

        if GeometryFigure(points, name_figure).get_square != 0:
            return GeometryFigure(points, name_figure)
        else:
            print("Введённые координаты образуют линию. Введите вершины заново")


def print_info(figure: GeometryFigure):
    print("\n")
    print(f"{figure.get_name}")
    print(f"Площадь фигуры: {figure.get_square}")
    print(f"Координаты:")
    figure.print_coordinates()


def move_figure(figure: GeometryFigure) -> GeometryFigure:
    print("Введите на какую длину по оси x y хотите сдвинуть фигуру")
    print("Указывайте отрицательные значения, если желаете двигать в протовоположную сторону направления оси")
    point = input_point()
    figure.move(point["x"], point['y'])
    return figure


def main():
    triangle = create_figure(3, "Треугольник")
    tetragon = create_figure(4, "Четырёхугольник")

    while True:
        print_menu()
        category = input_category()

        if category == 1:
            print_info(triangle)
            print_info(tetragon)
        elif category == 2:
            triangle = move_figure(triangle)
        elif category == 3:
            tetragon = move_figure(tetragon)
        elif category == 4:
            triangle.compare(tetragon)


if __name__ == "__main__":
    main()
