class Znak:

    def __init__(self, name: str, surname: str, zodiac: str, date_birth: list):
        self._name = name
        self._surname = surname
        self._zodiac = zodiac
        self._data_birth = date_birth

    def __str__(self):
        return f"{self._name} {self._surname} {self._zodiac} {self._data_birth[0]}" \
               f" {self._data_birth[1]} {self._data_birth[2]}"

    @property
    def get_data_birth(self):
        return self._data_birth

    @property
    def get_surname(self):
        return self._surname

class ArrayZnak:

    def __init__(self, array_znak: list):
        self._array_znak = array_znak
        self._streamline_array()

    def print_all_znak(self):
        for object in self._array_znak:
            print(object)

    def _streamline_array(self):
        self._array_znak.sort(
            key=lambda object: (object.get_data_birth[2], object.get_data_birth[1], object.get_data_birth[0]))

    def search_znak(self, surname: str):

        list_object = []                        # поиск студента через какое-либо поле: имя или фамилия и тд
                                                # так как имена не уникальны, то возращается список студентов
        for object in self._array_znak:
            if object.get_surname == surname:
                list_object += [object]

        return list_object


