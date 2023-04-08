from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    paths_table = [[0 for _ in range(m)] for _ in range(n)]  # Создаем пустую таблицу размером n*m

    for j in range(m):  # Заполняем первую строку таблицы единицами
        paths_table[0][j] = 1
    for i in range(n):  # Заполняем первый столбец таблицы единицами
        paths_table[i][0] = 1

    # Заполняем остальные ячейки таблицы
    for i in range(1, n):
        for j in range(1, m):
            paths_table[i][j] = paths_table[i - 1][j] + paths_table[i][j - 1] + paths_table[i - 1][j - 1]

    return paths_table


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
# пустая строка
