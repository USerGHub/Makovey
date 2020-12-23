#include <stdio.h>
#include <cmath>
#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>

extern "C" {

class Node {
    public:
        int position[2];
        std::vector<Node> parent{};
        // 3 как время прохождения клетки
        int cost = 3;
        int g = 0;  // стоимость пути от начальной вершины
        int f = 0;  // минимальная стоимость перехода в соседний узел

        friend bool operator==(const Node &n1, const Node &n2) {
        if (n1.position == n2.position)
            return true;
        else return false;
    }
};

std::vector<std::vector<int>> returnPath(Node current_node, std::vector<std::vector<int>> maze) {
    std::vector<int> path;
    std::vector<int> cost;
    int no_rows    = maze.size();
    int no_columns = maze[0].size();

    Node current = current_node;
    while (current.parent.size() > 0) {
        path.push_back(*current.position);
        cost.push_back(current.cost);
        current = current.parent[0];
    }
    return {path,cost};
}

std::vector<std::vector<int>> search(std::vector<std::vector<int>> maze, int* start, int* end) {
    // Создание начального и конечного узлов
    Node start_node;
    memcpy(start_node.position, start, sizeof(int)*2 );
    Node end_node;
    memcpy( end_node.position, end, sizeof(int)*2 );

    // Инициирование списков посещенных и непосещенных узлов
    std::vector<Node> yet_to_visit_list;
    yet_to_visit_list.push_back(start_node);
    std::vector<Node> visited_list;

    // Возможные движения
    int move[8][2] =   {{-1, 0},
                        { 0,-1},
                        { 1, 0},
                        { 0, 1},
                        { 1, 1},
                        {-1, 1},
                        { 1,-1},
                        {-1,-1}};

    // Получаем количество строк и столбцов
    int no_rows    = maze.size();
    int no_columns = maze[0].size();
    
    // Зацикливаем, пока не найдет конечную точку
    while (yet_to_visit_list.size() > 0) {
      
        Node current_node = yet_to_visit_list.back();
        int current_index = 0;
        for (int i=0; i<yet_to_visit_list.size(); i++) {
            if (yet_to_visit_list[i].f < current_node.f) {
                current_node = yet_to_visit_list[i];
                current_index = i;
            }
        }
        // Удаляем выбранный узел из «списка посещений» и добавляем в список уже посещенных
        yet_to_visit_list.erase(yet_to_visit_list.begin() + current_index);
        visited_list.push_back(current_node);


        // Теперь проверяем, был ли найден целевой квадрат. Если ответ положительный, вызываем функцию path
        if (current_node.position == end_node.position) {
            return returnPath(current_node, maze);
        }

        // Для выбранной вершины находим все дочерние элементы
        std::vector<Node> children;
        for (int i=0; i<8; i++) {
            int node_position[2] = {current_node.position[0] + move[i][0],
                                    current_node.position[1] + move[i][1]
                                   };

            

                        // Проверка на выход за границы
            if ((node_position[0] > (no_rows - 1)) ||
                (node_position[0] < 0) ||
                (node_position[1] > (no_columns - 1)) ||
                (node_position[1] < 0)) {
                    continue;
            }

            // На случай заблокированного прохода
            if (maze[node_position[0]][node_position[1]] == -1) {
                continue;
            }

            // Добавляем новый узел
            int new_cost = maze[node_position[0]][node_position[1]];
            Node* new_node = new Node;
            new_node->position[0] = node_position[0];
            new_node->position[1] = node_position[1];
            new_node->parent.push_back(current_node);
            new_node->cost = new_cost;
            children.push_back(*new_node);
                              
        }

        // Для всех дочерних элементов
        for (Node &child : children) {
            // ////
            // if (child.position == visited_list.back().position) {
            //     std::cout << 1 << std::endl;
            // }
            // ////
            // Если уже есть в посещенных узлах, то игнорируем
            if (std::find(visited_list.begin(), visited_list.end(), child) != visited_list.end()) {
                
                continue;
            }
            
            // Определяем значения f, g
            child.g = current_node.g + child.cost;
            child.f = child.g;
            
            // Если узел уже есть в посещенных, но ранее длина была меньше -- игнорируем
            if (std::find(yet_to_visit_list.begin(), yet_to_visit_list.end(), child) != yet_to_visit_list.end()) {
                int index;
                index = std::find(yet_to_visit_list.begin(), yet_to_visit_list.end(), child) - yet_to_visit_list.begin();
                if (child.g >= yet_to_visit_list[index].g) {
                    continue;
                }
            }
            
            yet_to_visit_list.push_back(child);
        }
    }
    return {{0}};
}   


int main() {
    std::vector<std::vector<int>> a = {{1,0,1},{0,1,1},{1,0,1}};
    int  b[2] = {0,1};
    int  c[2] = {0,2};
    std::vector<std::vector<int>> d = search(a,b,c);
    // for (auto row : d) {
    //     for (auto col : row) {
    //         std::cout << d.size() << std::endl;
    //     }
    // }
    return 0;
}








}

// Компиляция осуществляется :
// gcc -shared -Wl,-soname,$name -o $name.so -fPIC $name.cpp