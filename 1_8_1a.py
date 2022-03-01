import math


def print_formula():  # показывает формулы, через которые ввёлся подсчёт
    print("Необходимо посчитать данный интеграл: w = ∫(a->b) f(x)dx")
    print("Подсчёт ведётся через формулу левых прямоугольников: S=h * Σ( (i=0 -> n-1) f(a + ih) ), где h = (b-a)/n")
    print("n - количество отрезков, на которые разбивается предел интегрирование (n >= 1)")
    print("Подынтегральная функция: sin(x)/(1+x^2)")

def story(count, story_input):  # показывает историю ввода

    if (count == 0):
        print("Нет введённых данных")
        return

    print(f"Всего вводов: {count}")
    for i in range(0, count):
        print(f"\nВвод №{i + 1}:")
        print(f"Пределы интегрирования: {story_input[i][0]} -> {story_input[i][1]}")
        print(f"Количество отрезков: {story_input[i][2]}")
        print(f"Результат интергала: {story_input[i][3]}")


def get_input_switch_variable():  # ввод выбора пункта из меню
    while True:
        try:
            switch_variable = int(input())
            if switch_variable > 0 and switch_variable <= 4:
                return switch_variable
            else:
                print('Неверно введено число. Введите "1", "2", "3" или "4" ')
        except ValueError:
            print("Неверно выполнен ввод. Введите одно целое число")


def get_input_limit():  # ввод предела интегрирования
    print("Введите через пробел нижний и верхний пределы интегрирования: ", end="")
    while True:
        try:
            a, b = map(float, input().split())
            if (a <= b):
                return a, b
            else:
                print("Неверно введены пределы интегрирования. Первое число должно быть меньше второго")

        except ValueError:
            print("Неверно выполнен ввод. Введите числа")


def get_input_n():  # ввод количества отрезков, на которые будет разделён предел интегрирования
    print("На сколько частей разбить отрезок интегрирования: ", end="")
    while True:
        try:
            n = int(input())
            if (n >= 1):
                return n
            else:
                print("Невверно введено число (n >= 1)")
        except ValueError:
            print("Неверно выполнен ввод. Введите одно целое число")


def f(x):  # считает значение функции в указанной точке
    return math.sin(x) / (1 + math.pow(x, 2))


def formula_result(a, h, n):  # считает результат интеграла
    summa = 0
    for i in range(0, n):
        summa += f(a + i * h)
    return summa * h


def print_result(result):  # показывает результат интеграла
    print(f"Итоговый результат интеграла: {result}")


def integral(count, story_input):  # подсчёт значения интеграла

    a, b = get_input_limit()
    n = get_input_n()

    h = (a - b) / n
    result = formula_result(a, h, n)
    print_result(result)

    count += 1  # перезапись истории ввода
    story_input += [[a, b, n, result]]  # по индексам 0 - нижний предел интегрирование, 1 - верхний предел интегрирования
                                        # 2 - кол-во отрезков, 3 - результат интеграла
    return count, story_input


def print_menu():
    print("\nМеню:")
    print("1 - формулы, по которым ведётся подсчёт")
    print("2 - посчитать интеграл")
    print("3 - вывод истории вводов")
    print("4 - выйти из программы")


def main():
    count = 0
    story_input = []

    while True:
        print_menu()

        switch_variable = get_input_switch_variable()

        if switch_variable == 1: print_formula()
        elif switch_variable == 2: count, story_input = integral(count, story_input)
        elif switch_variable == 3: story(count, story_input)
        elif switch_variable == 4: quit()


if __name__ == "__main__":
    main()

