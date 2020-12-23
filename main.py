import sys
from random import random
from time import time
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
        self.outputButton.setText('')
        # Технические средства нарушителя
        # [Кусачки, Поддельный пропуск, Огнестрельное оружие] 
        # !!! 1 -- это отсутствие
        self.intruder_have = [1,1,1]
        # Коэффициент осведомленности
        path.step_cost = 3*0.6
        self.knowledge_box.currentIndexChanged.connect(self.knowledgeChange)


        # Отрисовка дополнительных компонентов
        self.UiComponents()
        # 

        #
        #
        self.show()

    # Функция добавления дополнительных элементов
    def UiComponents(self, cols=45, rows=47):

        # Рисуем поле
        self.field = []
        for col in range(cols):
            self.field.append([])
            for row in range(rows):
                cell = Cell(self, row, col)
                cell.move(1+14*row,40+14*col)
                cell.clicked.connect(cell.click)
                self.field[-1].append(cell)
        #
        # Кнопка вызова справки
        self.helpGroundButton.clicked.connect(self.groundHelp)
        # Кнопка вызова полного отчета
        self.outputButton.clicked.connect(self.fullReport)
        # Кнопка расчета критического пути
        self.actionButton.clicked.connect(self.findPath)
        # Кнопка очистки нарисованых путей
        self.clearButton.clicked.connect(self.clearPath)
        # Кнопка сохранения
        self.saveButton.clicked.connect(lambda: saving.save(self,self.field))
        self.saveButton.setIcon(QIcon('pictures/save.png'))
        # Кнопка загрузки
        self.loadButton.clicked.connect(lambda: saving.load(self))
        self.loadButton.setIcon(QIcon('pictures/open.png'))
        # Кнопка технических средств нарушителя
        self.intruder_tech_button.clicked.connect(self.changeTech)
        # Скрыть кнопки настроек нарушителя
        self.intruder_add_tech_list.setVisible(False)
        # Привязка функций на кнопки тех средств нарушителя
        self.intruder_add_tech_list.itemDoubleClicked.connect(self.addTech)
        # Удаление элемента по двойному щелчку
        self.intruder_tech_list.itemDoubleClicked.connect(self.removeTech)


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

        self.start_time = time()
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
        self.intruder_cost = [np.inf] # Задаем бесконечность для последующего уменьшения
        intruder_least_path = None
        try:
            for start_node in start_nodes:
                for end_node in end_nodes:
                    search_result = path.search(matrix_intruder, start_node, end_node)
                    total_path, total_cost = search_result[0], search_result[1] # Последнее число в total_cost равно всем затратам на путь
                    if total_cost[-1] < self.intruder_cost[-1]:
                        self.intruder_cost = total_cost
                        intruder_least_path = total_path
        except:
            self.outputButton.setText('Нет пути нарушитель-ПФЗ')
                    
        tg_least_path = None
        # Ищем критический путь для ТГ
        path.step_cost = 3 # Костыль
        # Последовательная тактика
        if self.consistentTactic.isChecked():
            try:
                search_result = path.search(matrix_tg, self.startTG_coordinate, self.endTG_coordinate)
                tg_least_path, self.tg_cost = search_result[0], search_result[1]
            except:
                with open('logs', 'a') as log_file:
                    log_file.write('Ошибка ТГ: последовательная тактика\n')
                    log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
                
        # С выходом на рубеж
        elif self.intermediateTactic.isChecked():
            try:
                # Объявление точки обнаружения
                self.detect_point = None
                self.time_before_detect = None
                # Находим путь ТГ
                search_result = path.search(matrix_tg, self.startTG_coordinate, self.endTG_coordinate)
                tg_least_path, self.tg_cost = search_result[0], search_result[1]
                # Ищем средства обнаружения на пути нарушителя
                for position in intruder_least_path:
                    cell = self.field[position[0]][position[1]]
                    if cell.detect_prob != 1:
                        # Проверяем, сработало ли средство
                        if cell.detect_prob < random():
                            # Помечаем точку обнаружения
                            self.detect_point = position
                            # Находим точку, где была ТГ в момент срабатывания
                            facility_index = intruder_least_path.index(position)
                            path_cost = self.intruder_cost[facility_index]
                            for i,cost in enumerate(self.tg_cost):
                                if cost >= path_cost:
                                    self.tg_cost = self.tg_cost[:i]
                                    tg_least_path = tg_least_path[:len(self.tg_cost)]
                                    break
                            # Время обнаружения
                            self.time_before_detect = path_cost
                            if len(self.tg_cost) == 0:
                                self.tg_cost = [0]

                            # ТГ реагирует в момент обнаружения нарушителя
                            self.tg_cost[-1] = path_cost 
                            # Ищем путь от точки, где была ТГ до средства обнаружения до средства обнаружения
                            # Реверс из-за ошибки с x-y
                            search_result = path.search(matrix_tg_fast, tg_least_path[-1][::-1], (cell.x, cell.y))
                            tg_least_path = tg_least_path[:-1] + search_result[0]
                            self.tg_cost = self.tg_cost + [cost + self.tg_cost[-1] for cost in search_result[1]]
                            # Дальше отправляем ТГ по следу нарушителя
                            for point in intruder_least_path[facility_index+1:]:
                                tg_least_path.append(point)
                                point_cost = self.field[point[0]][point[1]].cost[2]
                                self.tg_cost.append(self.tg_cost[-1]+point_cost+path.step_cost)
            
            except:
                with open('logs', 'a') as log_file:
                    log_file.write('Ошибка ТГ: тактика выход на рубеж\n')
                    log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
        self.knowledgeChange() # Конец костыля
        
        # Находим точку пересечения нарушителя и ТГ
        try:
            self.meet_point = self.detectIntruder(intruder_least_path, self.intruder_cost, tg_least_path, self.tg_cost)
        except:
            with open('logs', 'a') as log_file:
                log_file.write('Ошибка взаимодействия ТГ и нарушителя\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')

        try:
            # Отрисовка найденого пути
            self.drawPath(intruder_least_path, tg_least_path) 
            # Вывод длины наименьшего пути
            self.outputButton.setText(f'Время пути нарушителя: {self.intruder_cost[-1]:.2f} сек.')

            self.outputButton.setText(f'{self.outputButton.text()}\n'
                                     f'Время пути ТГ: {self.tg_cost[-1]:.2f} сек.')
            # Минимальная разница во времени между ТГ и нарушителем
            if self.cost_differents:
                self.cost_differents.sort()
                different = self.cost_differents[0]
                if different[1] == '+':
                     self.outputButton.setText(f'{self.outputButton.text()}\n'
                                              f'ТГ опоздала на {different[0]:.2f} сек.')
                elif different[1] == '-':
                    self.outputButton.setText(f'{self.outputButton.text()}\n'
                                              f'ТГ поспешила на {different[0]:.2f} сек.')
            else:
                self.outputButton.setText(f'{self.outputButton.text()}\n'
                                        f'Нарушитель задержан в точке ({self.meet_point[1]+1},{self.meet_point[0]+1})')


        except:
            with open('logs', 'a') as log_file:
                log_file.write('Путь не найден\n')
                log_file.write('Ошибка:\n' + traceback.format_exc() + '\n\n')
        
        self.end_time = time()
        

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
            path_indicator.move(4+14*x,43+14*y)
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
                path_indicator.move(4+14*x,43+14*y)

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
            self.outputButton.setText('')
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
        # Время до обнаружения нарушителя
        self.time_before_meet = None
        for node in tg_path:
            # Локальная переменная для вычисления наименьшей разницы во времени
            cost_different = None

            if node in intruder_path:
                intruder_index = intruder_path.index(node)
                tg_index = tg_path.index(node)
                cost_different = self.tg_cost[tg_index]-self.intruder_cost[intruder_index]
                if cost_different < 0:
                    self.cost_differents.append((-cost_different, '-'))
                else:
                    self.cost_differents.append((cost_different, '+'))
                # Если встретились в одно время в одном месте, то запоминаем место
                # Делаем небольшой промежуток по времени, чтобы не было жесткого условия равенства
                # у которого есть шанс не выполняться
                if intruder_index+1 < len(self.intruder_cost):
                    if (self.tg_cost[tg_index] <= self.intruder_cost[intruder_index+1] and
                        self.tg_cost[tg_index] >= self.intruder_cost[intruder_index]):
                        self.cost_differents = None
                        self.time_before_meet = self.intruder_cost[intruder_index]
                        return node
                else:
                    if (self.tg_cost[tg_index] <= self.intruder_cost[intruder_index] and
                        self.tg_cost[tg_index] >= self.intruder_cost[intruder_index-1]):
                        self.cost_differents = None
                        self.time_before_meet = self.intruder_cost[intruder_index]
                        return node
                if tg_index+1 < len(self.tg_cost):
                    if (self.intruder_cost[intruder_index] <= self.tg_cost[tg_index+1] and
                        self.intruder_cost[intruder_index] >= self.tg_cost[tg_index]):
                        self.cost_differents = None
                        self.time_before_meet = self.intruder_cost[intruder_index]
                        return node
                else:
                    if (self.intruder_cost[intruder_index] <= self.tg_cost[tg_index] and
                        self.intruder_cost[intruder_index] >= self.tg_cost[tg_index-1]):
                        self.cost_differents = None
                        self.time_before_meet = self.intruder_cost[intruder_index]
                        return node

    # Отрисовываем место встречи
    def drawMeeting(self, point):
        self.meet_indicator = QPushButton(self)
        self.meet_indicator.resize(15,15)
        self.meet_indicator.move(14*point[1],40+14*point[0])
        self.meet_indicator.setText('✘')
        self.meet_indicator.setStyleSheet('''QPushButton {background-color: white;
            font-size: 16px; font-weight: bold; color: red; border-color:  black; border-radius: 5}''')
        self.meet_indicator.show()
        self.meet_indicator.raise_()


    # Вывод справки
    def groundHelp(self):
               
        dialog = QDialog(self)
        dialog.setWindowTitle('Справка')
        dialog.resize(800,450)
        dialog.label = QLabel(dialog)
        help_text = '''Слабый грунт тип 1: грунт растительного слоя без корней и примесей; торф без корней; лёсс, песок и суспесь без примесей;
        
Слабый грунт тип 2: песок и суспесь с примесями гравия, гальки, валунов до 10% по объему; грунт растительного слоя с корнями примесью гальки или гравия; торф с корнями кустарника, чернозем мягкий с корнями кустарника;
        
Средний грунт тип 1: глина жирная и мягкая с примесью гальки до 10%; суглинок тяжелый без примесей; 
    
Средний грунт тип 2: чернозем отвердевший; суспесь с примесью более 30% по объему, лёсс отвердевший; гравийно-галечные грунты; 
    
Твердый грунт тип 1: глина тяжелая твердая; суглинок тяжелый и глина с примесью гальки, гравия, валунов; солончак отвердевший; 
    
Твердый грунт тип 2: ангидрит (гипс); гравийно-галечные грунты; 
    
Скальный грунт тип 1: туф; пемза, граниты; гнейсы (выветрившиеся дресвяные); гипс известняк мягкий; 
    
Скальный грунт тип 2доломит мягкий, известняк мергелистый; 
    
Скальный грунт тип 3: известняк мергелистый плотный; сланцы слюдяные, мрамор; граниты; гнейсы мелкозернистые.
            '''
        dialog.label.setText(help_text)
        dialog.label.setWordWrap(True)
        dialog.label.move(10,30)
        dialog.label.resize(780,390)
        dialog.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        dialog.button = QPushButton(dialog)
        dialog.button.clicked.connect(dialog.hide)
        dialog.button.move(360,420)
        dialog.button.resize(75,30)
        dialog.button.setText('✓ OK')
        dialog.exec_()

# Добаление тех средств нарушителю
# Открыть/скрыть меню
    def changeTech(self,tech=None):
        objects = [self.intruder_add_tech_list,self.knowledge_text,self.knowledge_box]
        for object in objects:
            object.setVisible(not object.isVisible())
    
    def addTech(self):
        tech = self.intruder_add_tech_list.currentItem().text()
        list_text = []
        for i in range(self.intruder_tech_list.count()):
            list_text.append(self.intruder_tech_list.item(i).text())

        if tech == 'Кусачки по металлу':
            if tech not in list_text:
                self.intruder_tech_list.addItem(tech)
                self.intruder_have[0] = 0.6
                for col in self.field:
                    for row in col:
                        if row.received_code[0] == 12:
                            row.cellProcess(row.received_code)

        elif tech == 'Поддельный пропуск':
            if tech not in list_text:
                self.intruder_tech_list.addItem(tech)
                self.intruder_have[1] = 0
                for col in self.field:
                    for row in col:
                        if row.received_code[0] in (1,2):
                            row.cellProcess(row.received_code)

        elif tech == 'Огнестрельное оружие':
            if tech not in list_text:
                self.intruder_tech_list.addItem(tech)
                self.intruder_have[2] = 0
                for col in self.field:
                    for row in col:
                        if row.modifies_flags['metal'] == 1:
                            row.cellProcess(row.received_code)

# Удаление тех средств нарушителя
    def removeTech(self):
        item = self.intruder_tech_list.takeItem(self.intruder_tech_list.currentRow())
        tech = item.text()
        if tech == 'Кусачки по металлу':
            self.intruder_have[0] = 1
            for col in self.field:
                for row in col:
                    if row.received_code[0] == 12:
                        row.cellProcess(row.received_code)
        elif tech == 'Поддельный пропуск':
            self.intruder_have[1] = 1
            for col in self.field:
                for row in col:
                    if row.received_code[0] in (1,2):
                        row.cellProcess(row.received_code)

        elif tech == 'Огнестрельное оружие':
            self.intruder_have[2] = 1
            for col in self.field:
                    for row in col:
                        if row.modifies_flags['metal'] == 1:
                            row.cellProcess(row.received_code)

# Изменение осведомленности
    def knowledgeChange(self):
        current_text = self.knowledge_box.currentText()
        if current_text == 'Высокий':
            path.step_cost = 0.6*3
        elif current_text == 'Средний':
            path.step_cost = 0.7*3
        elif current_text == 'Низкий':
            path.step_cost = 0.8*3          

# Вывод полного отчета
    def fullReport(self):
               
        dialog = QDialog(self)
        dialog.setWindowTitle('Отчет')
        dialog.resize(460,350)
        dialog.label = QLabel(dialog)
        report_text = []
        # Информация об обнаружении
        if self.intermediateTactic.isChecked():
            try:
                report_text.append(f'Точка обнаружения нарушителя ({self.detect_point[1]+1},{self.detect_point[0]+1})')
                report_text.append(f'Время обнаружения: {self.time_before_detect:.2f} сек.\n')
            except:
                report_text.append(f'Нарушитель не обнаружен\n')
        else:
            pass

        # Информация о задержании
        try:
            report_text.append(f'Нарушитель задержан в точке ({self.meet_point[1]+1},{self.meet_point[0]+1})')
            report_text.append(f'Время до задержания: {self.time_before_meet:.2f} сек.\n')
        except:
            report_text.append(f'Нарушитель не задержан\n')
        
        # Информация по нарушителю
        try:
            report_text.append(f'Время действия нарушителя:')
            report_text.append(f'\tполное: {self.intruder_cost[-1]:.2f} сек.')
            report_text.append(f'\tбез учета времени до первого обнаружения: {self.intruder_cost[-1]-self.time_before_detect:.2f} сек.')
            report_text.append(f'\tдо первого сигнала обнаружения: {self.time_before_detect:.2f} сек.\n')
        except:
            pass

        # Информация по ТГ
        try:
            report_text.append(f'Время действия сил реагирования:')
            report_text.append(f'\tполное: {self.tg_cost[-1]:.2f} сек.')
            report_text.append(f'\tбез учета времени на подготовку: {self.tg_cost[-1]-self.time_before_detect:.2f} сек.\n')
        except:
            pass

        # Информация по времени выполнения
        try:
            report_text.append(f'Время выполнения программы: {(self.end_time-self.start_time):.0f} сек.')
        except:
            pass

        report_text = '\n'.join(report_text)
        dialog.label.setText(report_text)
        dialog.label.setWordWrap(True)
        dialog.label.move(10,10)
        dialog.label.resize(440,290)
        dialog.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        dialog.button = QPushButton(dialog)
        dialog.button.clicked.connect(dialog.hide)
        dialog.button.move(200,310)
        dialog.button.resize(75,30)
        dialog.button.setText('✓ OK')
        dialog.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    app.exec_()

if __name__ == '__main__':
    main()
