class Student:

    def __init__(self, surname: str, name: str, patronymic: str, phone: str):
        self._student = {
            "name": name,
            "surname": surname,
            "patronymic": patronymic,
            "phone": phone
        }

    @property
    def getStudent(self) -> dict:
        return self._student

    def newField(self, typeField: str, subSting: str):
        self._student[typeField] = subSting

    def printStudent(self):
        print(self._student['surname'], self._student["name"], self._student["patronymic"], self._student["phone"], sep="   ")

class ListStudent:

    def __init__(self, listStudent: list):
        self._listStudents = listStudent

    def searchStudent(self, typeField: str, subString: str) -> list:

        listStudent = []                        # поиск студента через какое-либо поле: имя или фамилия и тд
                                                # так как имена не уникальны, то возращается список студентов
        for student in self._listStudents:
            if student.getStudent[typeField] == subString:
                listStudent += [student]

        return listStudent

    def searchUniqueStudent(self, phone) -> Student:  # поиск студента через ID, который в данном случае является номером телефона
        for student in self._listStudents:
            if student.getStudent["phone"] == phone:
                return student


    def deleteStudent(self, phone: str):
        self._listStudents.remove(self.searchUniqueStudent(phone))

    def addStudent(self, student: Student):
        self._listStudents.append(student)

    def sortListStudent(self, typeField: str):  # сортировка списка студентов
        self._listStudents.sort(key=lambda student: student.getStudent[typeField])

    def showStudents(self):  # показывает весь список студентов
        for student in self._listStudents:
            student.printStudent()

    @property
    def getList(self) -> list:
        return self._listStudents


class StudentGroup:

    def __init__(self, numberGroup: str, students: ListStudent):
        self._countStudent = len(students.getList)
        self._numberGroup = numberGroup
        self._listStudents = students

    @property
    def getListStudentObject(self) -> ListStudent:
        return self._listStudents

    def printInfoGroup(self):
        print(f'Группа номер {self._numberGroup}, количество студентов {self._countStudent}')

    def updateCountStudent(self):
        self._countStudent = len(self._listStudents.getList)

