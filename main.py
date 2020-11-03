import sys
from random import random
import traceback # Тестирование

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QDialog, QPushButton, QVBoxLayout, QLabel
import numpy as np

import design
import path
import saving
from cell import Cell

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Создание файла ошибок
        with open('logs', 'w') as log_file:
            pass
        # Координаты нарушителей
        self.intruders = []
        # Координаты ПФЗ
        self.PFZs = []
        # Координаты начальной точки ТГ
        self.startTG_coordinate = None
        # Координаты конечной точки ТГ
        self.endTG_coordinate = None
        # Ячейки с подкопами
        self.diggings = []
        # Строка вывода
        self.outputLabel.setText('')
        # Отрисовка дополнительных компонентов
        self.UiComponents()
        # 

        #
        #
        self.show()

    # Функция добавления дополнительных элементов
    def UiComponents(self, cols=44, rows=40):

        # Рисуем поле
        self.field = []
        for col in range(cols):
            self.field.append([])
            for row in range(rows):
                cell = Cell(self, row, col)
                cell.move(30+16*row,70+16*col)
                cell.clicked.connect(cell.click)
                self.field[-1].append(cell)
        #
        # Кнопка перелистывания окна инженерных средств
        self.listButton_next.clicked.connect(lambda: self.listMenu('next'))
        self.listButton_prev.clicked.connect(lambda: self.listMenu('prev'))
        # Кнопка вызова справки
        self.helpGroundButton.clicked.connect(self.groundHelp)
        # Кнопка расчета критического пути
        self.actionButton.clicked.connect(self.findPath)
        # Кнопка очистки нарисованых путей
        self.clearButton.clicked.connect(self.clearPath)
        # Кнопка сохранения
        self.saveButton.clicked.connect(lambda: saving.save(self,self.field))
        # Кнопка загрузки
        self.loadButton.clicked.connect(lambda: saving.load(self))


    # Функция бесконечного перелистывания инженерных средств
    def listMenu(self, direction):

        current_page = self.stackedWidget.currentIndex()
        max_pages = self.stackedWidget.count()
        if direction == 'next':
            current_page += 1
            if current_page > max_pages-1:
                current_page = 0
        else:
            current_page -= 1
            if current_page < 0:
                current_page = max_pages-1
        self.stackedWidget.setCurrentIndex(current_page)

    # Функция пересчета типа почвы в длину прохождения ячеек при подкопе
    def diggiCalculation(self, diggi_cells):
        for cell in diggi_cells:
            x = cell[1]
            y = cell[0]
            earth_cost = None
            current_text = self.chooseGroundBox.currentText()
            freeze_flag = self.freezeBox.isChecked()
            try:
                if current_text == 'Слабый грунт тип 1':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 4.3*3600
                    else:
                        self.field[x][y].cost[0] = 1*3600
                elif current_text == 'Слабый грунт тип 2':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 5.3*3600
                    else:
                        self.field[x][y].cost[0] = 1.45*3600
                elif current_text == 'Средний грунт тип 1':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 8.7*3600
                    else:
                        self.field[x][y].cost[0] = 1.45*3600
                elif current_text == 'Средний грунт тип 2':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 8.7*3600
                    else:
                        self.field[x][y].cost[0] = 2.1*3600
                elif current_text == 'Твердый грунт тип 1':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 10.2*3600
                    else:
                        self.field[x][y].cost[0] = 3.1*3600
                elif current_text == 'Твердый грунт тип 2':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 12.6*3600
                    else:
                        self.field[x][y].cost[0] = 3.1*3600
                elif current_text == 'Скальный грунт тип 1' or current_text == 'Скальный грунт тип 2' or current_text == 'Скальный грунт тип 3':
                    if freeze_flag:
                        self.field[x][y].cost[0] = 12.5*3600
                    else:
                        self.field[x][y].cost[0] = 12.5*3600
            except:
                with open('logs', 'a') as log_file:
                    log_file.write('Ошибка расчета времени подкопа\n')
                    log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
                

    # Функция поиска пути
    def findPath(self, start=None, end=None):

        # Оставляем место для последующих выводов
        # print('\n\n\n')
        # Обрабатываем почву для подкопов
        self.diggiCalculation(self.diggings)
        # Формируем матрицу из весов клеток
        matrix_intruder = [] # Для нарушителей
        matrix_tg = [] # Для тревожной группы
        matrix_tg_fast = [] # Для тревожной группы после обнаружения нарушителя
        # Массив из времени для каждого шага
        time_intruder = []
        time_tg = []
        for col in self.field:
            matrix_intruder.append([])
            matrix_tg.append([])
            matrix_tg_fast.append([])
            for row in col:
                matrix_intruder[-1].append(row.cost[0])
                matrix_tg[-1].append(row.cost[1])
                matrix_tg_fast[-1].append(row.cost[2])
        # print('\n'.join([''.join(["{:>3d}".format(item) for item in row])
        #     for row in matrix_tg_fast]))
        # print('\n\n')

        # Получаем координаты нарушителя
        try:
            start_nodes = []
            for intruder in self.intruders:
                start_nodes.append((intruder[0], intruder[1]))
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Ошибка в получении координат нарушителя\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

        # Получаем координаты ПФЗ
        try:
            end_nodes = []
            for PFZ in self.PFZs:
                end_nodes.append((PFZ[0], PFZ[1]))
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Ошибка в получении координат ПФЗ\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

        # Ищем все комбинации Нарушитель-ПФЗ
        intruder_cost = [np.inf] # Задаем бесконечность для последующего уменьшения
        intruder_least_path = None
        try:
            for start_node in start_nodes:
                for end_node in end_nodes:
                    search_result = path.search(matrix_intruder, start_node, end_node)
                    total_path, total_cost = search_result[0], search_result[1] # Последнее число в total_cost равно всем затратам на путь
                    if total_cost[-1] < intruder_cost[-1]:
                        intruder_cost = total_cost
                        intruder_least_path = total_path
        except:
            self.outputLabel.setText('Нет пути нарушитель-ПФЗ')
                    
        tg_least_path = None
        # Ищем критический путь для ТГ
        
        # Последовательная тактика
        if self.consistentTactic.isChecked():
            try:
                search_result = path.search(matrix_tg, self.startTG_coordinate, self.endTG_coordinate)
                tg_least_path, tg_cost = search_result[0], search_result[1]
            except:
                with open('logs', 'a') as log_file:
                    log_file.write('Ошибка ТГ: последовательная тактика\n')
                    log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
                
        # С выходом на рубеж
        elif self.intermediateTactic.isChecked():
            try:
                # Находим путь ТГ
                search_result = path.search(matrix_tg, self.startTG_coordinate, self.endTG_coordinate)
                tg_least_path, tg_cost = search_result[0], search_result[1]
                # Ищем средства обнаружения на пути нарушителя
                for position in intruder_least_path:
                    cell = self.field[position[0]][position[1]]
                    if cell.detect_prob != 1:
                        # Проверяем, сработало ли средство
                        if cell.detect_prob < random():
                            # Находим точку, где была ТГ в момент срабатывания
                            facility_index = intruder_least_path.index(position)
                            path_cost = intruder_cost[facility_index]
                            for i,cost in enumerate(tg_cost):
                                if cost >= path_cost:
                                    tg_cost = tg_cost[:i]
                                    tg_least_path = tg_least_path[:len(tg_cost)]
                                    break
                            if len(tg_cost) == 0:
                                tg_cost = [0]

                            # ТГ реагирует в момент обнаружения нарушителя
                            tg_cost[-1] = path_cost 
                            # Ищем путь от точки, где была ТГ до средства обнаружения до средства обнаружения
                            # Реверс из-за ошибки с x-y
                            search_result = path.search(matrix_tg_fast, tg_least_path[-1][::-1], (cell.x, cell.y))
                            tg_least_path = tg_least_path[:-1] + search_result[0]
                            tg_cost = tg_cost + [cost + tg_cost[-1] for cost in search_result[1]]
                            # Дальше отправляем ТГ по следу нарушителя
                            for point in intruder_least_path[facility_index+1:]:
                                tg_least_path.append(point)
                                point_cost = self.field[point[0]][point[1]].cost[2]
                                tg_cost.append(tg_cost[-1]+point_cost+path.step_cost)

            except:
                with open('logs', 'a') as log_file:
                    log_file.write('Ошибка ТГ: тактика выход на рубеж\n')
                    log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

        # Находим точку пересечения нарушителя и ТГ
        try:
            self.meet_point = self.detectIntruder(intruder_least_path, intruder_cost, tg_least_path, tg_cost)
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Ошибка взаимодействия ТГ и нарушителя\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

        try:
            # Отрисовка найденого пути
            self.drawPath(intruder_least_path, tg_least_path) 
            # Вывод длины наименьшего пути
            self.outputLabel.setText(f'Время пути нарушителя: {intruder_cost[-1]} сек.')
            self.outputLabel.setText(f'{self.outputLabel.text()}\n'
                                     f'Время пути ТГ: {tg_cost[-1]} сек.')
            # Минимальная разница во времени между ТГ и нарушителем
            if self.cost_differents:
                self.cost_differents.sort()
                different = self.cost_differents[0]
                if different[1] == '+':
                     self.outputLabel.setText(f'{self.outputLabel.text()}\n'
                                              f'ТГ опоздала на {different[0]} сек.')
                elif different[1] == '-':
                    self.outputLabel.setText(f'{self.outputLabel.text()}\n'
                                              f'ТГ поспешила на {different[0]} сек.')


        except:
            with open('logs', 'a') as log_file:
                log_file.write('Путь не найден\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
        

    # Функция отрисовки пути
    def drawPath(self, finded_intruder_path, finded_tg_path):
        
        # Очищаем прошлые пути
        self.clearPath()
        # Сделаем новые объекты для отображения иконок пути, чтобы по необходимости удалить
        self.intruder_path = []
        self.tg_path = []
        intruder_path_css = 'QPushButton {background-color: darkred; border-color: darkred ; border-radius: 3}'
        tg_path_css = 'QPushButton {background-color: darkblue; border-color: darkblue ; border-radius: 3}'
        # Только нарушитель
        for position in finded_intruder_path:
            x = position[1]; y = position[0]
            path_indicator = QPushButton(self)
            path_indicator.resize(7,7)
            path_indicator.move(34+16*x,74+16*y)

            # Вынесение на передний план
            path_indicator.show()
            path_indicator.raise_()

            path_indicator.setStyleSheet(intruder_path_css)
            self.intruder_path.append(path_indicator)

        # В случае наличия ТГ делаем аналогично для нее
        # Выносим в отдельный блок для случая, когда ТГ не может добрать до цели
        try:
            for position in finded_tg_path:
                x = position[1]; y = position[0]
                path_indicator = QPushButton(self)
                path_indicator.resize(7,7)
                path_indicator.move(34+16*x,74+16*y)

                # Вынесение на передний план
                path_indicator.show()
                path_indicator.raise_()

                path_indicator.setStyleSheet(tg_path_css)
                self.tg_path.append(path_indicator)
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Невозможно нарисовать путь тревожной группы\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
        
        # Рисуем точку пересечения Нарушителя и ТГ
        try:
            self.drawMeeting(self.meet_point)
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Нет места встречи нарушителя и ТГ\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

                
    # Функция очистки нарисованных путей
    def clearPath(self):
        try:
            for position in self.intruder_path:
                position.setParent(None)
            for position in self.tg_path:
                position.setParent(None)
            self.meet_indicator.setParent(None)
            del(self.meet_indicator)
        except:
            pass
    
    # Находим место обнаружения нарушителя
    def detectIntruder(self, intruder_path, intruder_cost, tg_path, tg_cost):
        # Глобальная переменная для вычисления наименьшей разницы во времени
        self.cost_differents = []
        for node in tg_path:
            # Локальная переменная для вычисления наименьшей разницы во времени
            cost_different = None

            if node in intruder_path:
                intruder_index = intruder_path.index(node)
                tg_index = tg_path.index(node)
                cost_different = tg_cost[tg_index]-intruder_cost[intruder_index]
                if cost_different < 0:
                    self.cost_differents.append((-cost_different, '-'))
                else:
                    self.cost_differents.append((cost_different, '+'))
                # Если встретились в одно время в одном месте, то запоминаем место
                # Делаем небольшой промежуток по времени, чтобы не было жесткого условия равенства
                # у которого есть шанс не выполняться
                if intruder_index+1 < len(intruder_cost):
                    if (tg_cost[tg_index] <= intruder_cost[intruder_index+1] and
                        tg_cost[tg_index] >= intruder_cost[intruder_index]):
                        self.cost_differents = None
                        return node
                else:
                    if (tg_cost[tg_index] <= intruder_cost[intruder_index] and
                        tg_cost[tg_index] >= intruder_cost[intruder_index-1]):
                        self.cost_differents = None
                        return node
                if tg_index+1 < len(tg_cost):
                    if (intruder_cost[intruder_index] <= tg_cost[tg_index+1] and
                        intruder_cost[intruder_index] >= tg_cost[tg_index]):
                        self.cost_differents = None
                        return node
                else:
                    if (intruder_cost[intruder_index] <= tg_cost[tg_index] and
                        intruder_cost[intruder_index] >= tg_cost[tg_index-1]):
                        self.cost_differents = None
                        return node

    # Отрисовываем место встречи
    def drawMeeting(self, point):
        self.meet_indicator = QPushButton(self)
        self.meet_indicator.resize(15,15)
        self.meet_indicator.move(30+16*point[1],70+16*point[0])
        self.meet_indicator.setText('✘')
        self.meet_indicator.setStyleSheet('''QPushButton {background-color: white;
            font-size: 16px; font-weight: bold; color: red; border-color:  black; border-radius: 5}''')
        self.meet_indicator.show()
        self.meet_indicator.raise_()


    # Вывод справки
    def groundHelp(self):
               
        dialog = QDialog(self)
        dialog.setWindowTitle('Справка')
        dialog.resize(450,300)
        dialog.label = QLabel(dialog)
        dialog.label.setText('Здесь какой то текст')
        dialog.label.move(10,30)
        dialog.label.resize(430,270)
        dialog.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        dialog.button = QPushButton(dialog)
        dialog.button.clicked.connect(dialog.hide)
        dialog.button.move(190,260)
        dialog.button.resize(75,30)
        dialog.button.setText('✓ OK')
        dialog.exec_()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    app.exec_()

if __name__ == '__main__':
    main()


# Исправилю ещё ошибки с x-y (пусть и не мешают, но некрасиво)
# Внимательно посмотрю, что можно улучшить
# и надо ли? По времени все на алгоритм все равно уходит
# Справку и подробный расчет взаимодействия

# !!!!!!!! Если увидишь ошибки или вдруг вылетит сразу пиши