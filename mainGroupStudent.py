from groupStudentClassModels import *
import re


def checkPhone(phone):
    numberRe = r'\d\(\d\d\d\)\d\d\d-\d\d-\d\d'
    if re.match(numberRe, phone) is not None:
        return True
    else:
        return False


def checkAttribut(attribut):
    nameRe = "[А-Яа-я]"
    if re.match(nameRe, attribut) is not None:
        return True
    else:
        return False


def printStartMenu():
    print('1 - Показать информацию о группе')
    print("2 - Показать список студентов")
    print("3 - Сортировать список студентов")
    print("4 - Добавить студента")
    print("5 - Удалить студента")
    print("6 - Поиск студентов")


def printCategoryAttribute(printPhone: bool):
    print("1 - По имени")
    print("2 - По фамилии")
    print("3 - По отчеству")
    if printPhone: print("4 - По телефону")


def inputCategoryMenu():
    while True:
        try:
            category = int(input("Выберите категорию: "))
            if category in range(1, 7):
                return category
            print("Введите одно целое число от 1 до 6")
        except ValueError:
            print("Некорректно введено значение")


def inputPhone():
    print("Введите номер телефона по шаблону X(XXX)XXX-XX-XX. Например 8(123)456-78-90")
    while True:
        phone = input("Номер: ")
        if checkPhone(phone):
            return phone
        else:
            print("Неккоректно введён номер телефона")


def inputCategoryAttribute(inputPhone: bool):
    while True:
        try:
            category = int(input("Выберите категорию: "))
            if category in range(1, 5):
                if category == 1:
                    return "name"
                elif category == 2:
                    return "surname"
                elif category == 3:
                    return "patronymic"
                elif category == 4 and inputPhone:
                    return "phone"
            print("Введите одно целое число от 1 до 4")
            if not inputPhone: print("Сортировать по номеру телефону нельзя")
        except ValueError:
            print("Некорректно введено значение")


def inputAttributStudent():
    print("Введите через пробел ФАМИЛИЮ ИМЯ ОТЧЕСТВО НОМЕР")
    print("Номер телефона введите по шаблону X-XXX-XXX-XX-XX. Например 8-123-456-78-90")
    while True:
        attributs = input().split()
        if not checkAttribut(attributs[0]):
            print("Неккоректно введена фамилия")
            continue

        if not checkAttribut(attributs[1]):
            print("Неккоректно введено имя")
            continue

        if not checkAttribut(attributs[2]):
            print("Неккоректно введено отчество")
            continue

        if not checkPhone(attributs[3]):
            print("Неккоректно введен номер телефона")
            continue

        return attributs


def inputAttribut():
    while True:
        attribut = input()
        if checkAttribut(attribut):
            return attribut
        else:
            print("Неккоректно введена подстрока")


def inputSearchSubString(phoneSearch):
    print("Введите подстроку, по которой осуществится поиск")
    if phoneSearch == "phone":
        return inputPhone()
    else:
        return inputAttribut()


def switchCategoryStartMenu(category, studentGroup: StudentGroup):
    if category == 1:
        studentGroup.printInfoGroup()

    elif category == 2:
        studentGroup.getListStudentObject.showStudents()

    elif category == 3:
        print("По какой категории сортировать список?")
        printCategoryAttribute(False)
        categotyAttribut = inputCategoryAttribute(False)
        studentGroup.getListStudentObject.sortListStudent(categotyAttribut)
        print("Список успешно отсортирован")

    elif category == 4:
        attributs = inputAttributStudent()
        studentGroup.getListStudentObject.addStudent(Student(*attributs))
        studentGroup.updateCountStudent()

    elif category == 5:
        phone = inputPhone()
        studentGroup.getListStudentObject.deleteStudent(phone)
        studentGroup.updateCountStudent()

    elif category == 6:
        print("По какой категории искать студентов?")
        printCategoryAttribute(True)
        categoryAttribut = inputCategoryAttribute(True)
        subString = inputSearchSubString(categoryAttribut)
        listStudent = studentGroup.getListStudentObject.searchStudent(categoryAttribut, subString)

        if len(listStudent) != 0:
            for student in listStudent: student.printStudent()
        else:
            print("Данных студентов нет в списке")

    return studentGroup


def createGroup() -> StudentGroup:
    f = open('students.txt', 'r', encoding="utf-8")
    students = []
    for line in f:
        students += [Student(*line.split())]

    listStudent = ListStudent(students)
    f.close()
    return StudentGroup("421-4", listStudent)


def main():
    studentGroup = createGroup()

    while True:
        printStartMenu()
        category = inputCategoryMenu()
        studentGroup = switchCategoryStartMenu(category, studentGroup)


if __name__ == "__main__":
    main()
