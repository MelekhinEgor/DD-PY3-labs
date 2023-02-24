"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало слева, конец справа
        """
        self._queue = []  # используем pyton list для организации очереди

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)  # добавляем элемент в список методом append (вставка элемента справа)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._queue:  # проверка очереди на наличие в ней элементов
            raise IndexError('Очередь пуста!')

        return self._queue.pop(0)  # извлечение первого элемента из очереди

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):  # проверка введенного индекса на целочисленность
            raise TypeError('Введенный индекс не целочисленный')

        if not 0 <= ind < len(self._queue):  # проверка индекса на нахождение в границах очереди
            raise IndexError('Индекс вне границ очереди')

        return self._queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self._queue.clear()  # очищаем очередь методом clear

    def __len__(self) -> int:
        """ Количество элементов в очереди. """
        return len(self._queue)
# пустая строка
