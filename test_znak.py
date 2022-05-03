from person_class import *

import re


def check_data(data: list):  # проверка правильности ввода даты

    data = [int(x) for x in data]

    if data[1] in (1, 3, 5, 7, 8, 10, 12) and (1 <= data[0] <= 31):  # месяцы с 31-им днем
        return True

    elif data[1] in (4, 6, 9, 11) and (1 <= data[0] <= 30):  # месяцы с 30-ю днями
        return True

    elif data[1] == 2 and (data[2] % 4 == 0 and data[2] % 100 != 0 and (1 <= data[0] <= 29) or
                           (data[2] % 4 != 0 or data[2] % 100 == 0) and (1 <= data[0] <= 28)):  # проверка февраля
        return True
    else:
        return False


def check_normal_char(string):
    nameRe = '[A-Za-zА-Яа-я]'
    if re.match(nameRe, string) is None:
        return False
    return True

def chek_zodiak(string: str):
    if string.lower() in ('овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы'):
        return True
    else:
        return False

def input_znak():
    while True:
        data = input("Ввод полей: ").split()
        try:
            if data == ['stop']:
                return False

            if len(data) != 6:
                print("Введены не все поля")
                continue


            for number in data[3:]:
                int(number)

            if not check_data(data[3:]):
                print("Неверно введены даты")
                continue

            if not chek_zodiak(data[2]):
                print("Такого знака зодиака не существует")
                continue

            for string in data[:3]:
                if not check_normal_char(string):
                    print("Введены недопустимые символы в полях ИМЯ ФАМИЛИЯ ЗОДИАК")
                    break

            return Znak(data[0], data[1], data[2], [data[3], data[4], data[5]])

        except ValueError:
            print("Неверно введены даты")
            continue


def create_array() -> ArrayZnak:
    array_znak = []
    while (True):

        znak_object = input_znak()
        if znak_object != False:
            array_znak += [znak_object]
            print("Объект добавлен")
        elif len(array_znak) == 0:
            print("Введено 0 объектов")
        else:
            print("Остановлено")
            return ArrayZnak(array_znak)


def print_menu():
    print("1 - показать все объекты")
    print("2 - найти человека по фамилии")


def input_category():
    while True:
        try:
            category = int(input("Выберите категорию: "))
            if category in range(1, 3):
                return category
            print("Введите одно целое число от 1 до 6")
        except ValueError:
            print("Некорректно введено значение")

def input_surname():
    while True:
        string = input("Введите фамилию: ")
        if check_normal_char(string):
            return string
        else:
            print("Введены недопустимые символы")
            continue

def main():
    print("Ввод данных объекта")
    print("Введите через пробел: ИМЯ ФАМИЛЯ ЗОДИАК ДЕНЬ МЕСЯЦ ГОД")
    print("Чтобы закончить ввод, введите stop")

    array_znak = create_array()

    while (True):
        print_menu()

        category = input_category()

        if category == 1:
            array_znak.print_all_znak()

        if category == 2:
            surname = input_surname()
            array_result = array_znak.search_znak(surname)

            if len(array_result) == 0:
                print("\nТакого человека в списке нет\n")
            for znak in array_result: print(f"\n{znak}\n")


if __name__ == "__main__":
    main()

