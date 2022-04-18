class MyDeque:
    _deque = []

    def push_front(self, element):  # добавить в начало
        self._deque = [element] + self._deque

    def push_back(self, element):  # добавить в конец
        self._deque += [element]

    def pop_back(self):  # удалить в конце
        if self._deque == []: return None
        return self._deque.pop()

    def pop_front(self):  # удалить в начале
        if self._deque == []: return None
        element = self._deque[0]
        del self._deque[0]
        return element

    def is_empty(self, element):

        if element in self._deque:
            return True
        else:
            return False

    def clear(self):
        self._deque.clear()

    def __str__(self):
        return str(self._deque)
