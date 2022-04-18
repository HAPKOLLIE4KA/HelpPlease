from deqeu_class import MyDeque
import random


def main():
    deque = MyDeque()

    for i in range(10):
        deque.push_front(random.randint(10, 99))

    print("Изначальная очередь")
    print(deque)

    print("\nДобавление в КОНЕЦ очереди случайного числа")
    deque.push_back(random.randint(10, 99))
    print(deque)

    print("\nдобавление в НАЧАЛО очереди случайного числа")
    deque.push_front(random.randint(10, 99))
    print(deque)

    print("\nУдаление элемента из КОНЦА очереди, а также получение удалённого элемента")
    element = deque.pop_back()
    print(deque)
    print(f"Удалёный элемент - {element}")

    print("\nУдаления элемента из НАЧАЛА очереди, а также получение удалённого элемента")
    element = deque.pop_front()
    print(deque)
    print(f"Удалённый элемент - {element}")

    print("\nПроверка на наличие случайного числа в очереди")
    element = random.randint(10, 99)
    print(f"Результат проверки наличия числа {element} в очереди - {deque.is_empty(element)}")

    print("\nОтчистка очереди")
    deque.clear()
    print(deque)


if __name__ == "__main__":
    main()
