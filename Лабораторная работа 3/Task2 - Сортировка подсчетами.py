from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container  # Если массив пустой, просто возвращаем его
    if any(num < 0 for num in container):
        raise ValueError("Массив должен содержать только неотрицательные числа")
    max_value = max(container)  # Определяем максимальное значение в массиве
    counts = [0] * (max_value + 1)  # Создаем массив для подсчета количества элементов
    for value in container:  # Подсчитываем количество каждого элемента в массиве
        counts[value] += 1
    result = []  # Создаем новый отсортированный массив на основе информации о количестве элементов
    for value in range(max_value + 1):
        count = counts[value]
        result.extend([value] * count)
    return result
# пустая строка
