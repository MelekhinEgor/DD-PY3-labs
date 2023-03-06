"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:  # проверка на пустой список
        raise ValueError('Список пуст')
    min_number = arr[0]  # начальные минмальные значение и индекс
    min_index = 0
    for i in range(len(arr)):  # проходимся по всем значениям
        if arr[i] < min_number:  # проверка текущего значения и минимального
            min_number, min_index = arr[i], i  # переприсваивание минимальных значения и индекса
    return min_index
# пустая строка
