# Функция поиска кратчайшего пути
# Алгоритм A*
# https://ru.wikipedia.org/wiki/A*

# Реализация копируется внаглую отсюда:
# https://medium.com/nuances-of-programming/%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0-a-3bb59be05a79

import numpy as np
from random import random

# 3 как время прохождения клетки
step_cost = 3

# Класс узла
class Node:
    def __init__(self, parent = None, position = None, cost = 0):
        self.parent = parent
        self.position = position
        # 3 как время прохождения клетки
        self.cost = cost + step_cost

        self.g = 0  # стоимость пути от начальной вершины
        # !!! Попробуем проигнорировать переменную h, так как по сути не нужна
        # self.h = 0  # эвристическое приближение стоимости пути от узла до конечного узла
        self.f = 0  # минимальная стоимость перехода в соседний узел

    def __eq__(self, other):
        return self.position == other.position


# Функция пути
def returnPath(current_node, maze):
    path = []
    cost = [0]
    no_rows, no_columns = np.shape(maze)

    # Инициируем лабиринт с (-1) в каждой клетке
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]

    current = current_node
    while current is not None:
        path.append(current.position)
        cost.append(current.cost + cost[-1])
        current = current.parent
    # Реверс пути для отображения по ходу движения
    path = path[::-1]
    # Реверс затрат
    cost = cost[1:-1]
    cost = [cost[-1]-i for i in [0]+cost][::-1]
    
    return path, cost

# Функция поиска пути
def search(maze, start, end):

    # Создание начального и конечного узлов
    # ! Что-то не так с x,y поэтому меняю местами
    start_node = Node(None, tuple(start[::-1]))
    end_node = Node(None, tuple(end[::-1]))

    # Инициирование списков посещенных и непосещенных узлов
    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(start_node)

    # Задаем стоп-условие
    outher_iterations = 0
    max_iterations = (len(maze)//2)**10

    # Возможные движения
    move = [[-1, 0],
            [ 0,-1],
            [ 1, 0],
            [ 0, 1],
            [ 1, 1],
            [-1, 1],
            [ 1,-1],
            [-1,-1]]

    # Получаем количество строк и столбцов
    no_rows, no_columns = np.shape(maze)

    # Зацикливаем, пока не найдет конечную точку
    while len(yet_to_visit_list) > 0:
        outher_iterations += 1
        # Получаем текущую точку
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # Если не пришли к точке, но цена уже слишком высока)))
        # По тестам ни разу не выскочило, но пока оставим
        if outher_iterations > max_iterations:
            print('Миссия провалена')
            return(returnPath(current_node, maze))

        # Удаляем выбранный узел из «списка посещений» и добавляем в список уже посещенных
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # Теперь проверяем, был ли найден целевой квадрат. Если ответ положительный, вызываем функцию path
        if current_node == end_node:
            return returnPath(current_node, maze)


        # Для выбранной вершины находим все дочерние элементы
        children = []
        for new_position in move:

            # Получаем возможные узлы
            node_position = (current_node.position[0] + new_position[0],
                            current_node.position[1] + new_position[1])
            # Проверка на выход за границы
            if (node_position[0] > (no_rows - 1) or
                node_position[0] < 0 or
                node_position[1] > (no_columns - 1) or
                node_position[1] < 0):
                continue

            # На случай заблокированного прохода
            if maze[node_position[0]][node_position[1]] == -1:
                continue
            
            # Добавляем новый узел
            new_cost = maze[node_position[0]][node_position[1]]
            new_node = Node(current_node, node_position, new_cost)
            children.append(new_node)

        # Для всех дочерних элементов
        for child in children:

            # Если уже есть в посещенных узлах, то игнорируем
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            # Определяем значения f, g, h
            child.g = current_node.g + child.cost
            # Игнорируем h
            # child.h = (((child.position[0] - end_node.position[0])**2) +
            #             ((child.position[1] - end_node.position[1])**2))
            child.f = child.g # + child.h

            # Если узел уже есть в посещенных, но ранее длина была меньше -- игнорируем
            if len([i for i in yet_to_visit_list if child == i and child.g >= i.g]) > 0:
                continue

            # Добавляем дочерний узел в список посещенных
            yet_to_visit_list.append(child)
                

# Оставим, чтобы при изменениях в случае необходимости протестить все в консоли
# if __name__ == "__main__":

    # maze = []
    # for i in range(5):
    #     maze.append([])
    #     for j in range(5):
    #         maze[-1].append(int(random()*5))

    # maze = [[1,1,1,1,1],
    #         [1,1,5,1,1],
    #         [1,1,5,1,1],
    #         [1,1,5,1,1]]
    # start = (1, 3)
    # end = (4, 1)

    # path = search(maze,start,end)
    # print('\n'.join([''.join(["{:>3d}".format(item) for item in row])
    #         for row in path[0]]))
    # print(path[1])
