
# вершины представляются в виде массива словарей, содержащих два поля: "x" "y"

class GeometryFigure():

    def __init__(self, _points, name):
        self._name_figure = name
        self._points = _points
        self._count_punkt = len(_points)
        self._square = self._calculation_square()

    @property
    def get_square(self):
        return self._square

    @property
    def get_name(self):
        return self._name_figure

    def print_coordinates(self):
        for index, coordinates in enumerate(self._points):
            print(f"Вершина {index + 1}: {coordinates['x']}, {coordinates['y']}")

    def move(self, x, y):
        for index, coordinates in enumerate(self._points):
            self._points[index] = {
                "x": coordinates["x"] + x,
                "y": coordinates["y"] + y
            }

    def compare(self, figure):
        if self._square > figure.get_square:
            print(f"Площадь фигуры {self._name_figure} больше площади {figure.get_name}")
        elif self._square == figure.get_square:
            print("Площади фигур равны")
        else:
            print(f"Площадь фигуры {figure.get_name} больше площади {self._name_figure}")

    def _calculation_square(self):  # подсчёт площади через формулу Гаусса
        summa = 0

        for i in range(self._count_punkt):
            point1 = self._points[i]["x"]
            point2 = self._points[0]["y"] if i + 1 == self._count_punkt else self._points[i + 1]["y"]
            point3 = self._points[self._count_punkt - 1]["y"] if i == 0 else self._points[i - 1]["y"]

            summa += point1 * (point2 - point3)

        return (1 / 2) * abs(summa)
