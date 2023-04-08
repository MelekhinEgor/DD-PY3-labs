from typing import Union, List

import networkx as nx


def generate_graph(way_wight: List[int]) -> nx.DiGraph:
    """
    Функция формирующая взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    Исходными данными для которого является список целых чисел, явялющихся весами дуг, связывающих узлы графа

    :param way_wight: Веса дуг, являющиеся стоимостью, которую необходимо заплатить, чтобы наступить на ступень
    :return: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    """
    dot = len(way_wight)  # Находим количество дуг
    graph = nx.DiGraph()  # Создаем пустой граф
    for i in range(dot):
        for j in range(i+1, min(dot, i+3)):
            graph.add_edge(i, j, weight=way_wight[j])  # Задаем дуги, связывающий графы, с заданным весом
    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # Алгоритм Дейкстра для поиска дешевого пути
    return nx.dijkstra_path_length(graph, source=0, target=graph.number_of_nodes()-1)


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = generate_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
# пустая строка
