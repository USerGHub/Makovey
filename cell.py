from PyQt5.QtWidgets import QPushButton

# Класс клетки на поле 
class Cell(QPushButton):
    def __init__(self, parent, x, y, k=1):
        super(Cell, self).__init__(parent)
        self.resize(13,13)

        # Свойства ячейки
        self.k = k # Коэффициент осведомленности
        # На путь между клетками тратится 3 сек
        self.cost = [0,0,0] # Первое число для нарушителя, второе – для ТГ, третье – для движения ТГ по следам нарушителя
        self.x = x
        self.y = y

        # Наличие модификаторов
        self.modifies = []
        # Флаги (булианы): емкостное, радио, видео, стекло
        self.modifies_flags = { 'video': 0,
                                'glass': 0,
                                'capacity': 0,
                                'radio': 0,
                                'ir': 0,
                                'bomb': 0,
                                'warm': 0,
                                'gerkon': 0,
                                'piezo': 0,
                                'metal': 0}
        # Шанс необнаружения
        self.detect_prob = 1

        # Принимаем сигналы об основных объектов в виде пары чисел
        # для упрощения сохранения/загрузки файлов
        # первое число – какое средство использовалось, второе – его свойства
        self.received_code = [None, None]

        # CSS стиль ячейки
        self.default_style = 'QPushButton {background-color: rgb(210,210,210); border-color:  black; border-radius: 3}'
        self.style = self.default_style
        self.setStyleSheet(self.default_style)

    def click(self):
        # 
        # Стоимость подкопов расчитывается в основном файле
        #
        
        #
        # Средства обнаружения (модификаторы)
        #
        if self.parent().videoFacility.isChecked():
            # Видеокамера
            self.modifies_flags['video'] = 1

        if self.parent().glassFacility.isChecked():
            # Датчик разбития стекла
            if self.received_code[0] == 9:
                self.modifies_flags['glass'] = 1
                
        if self.parent().capacityFacility.isChecked():
            # Емкостное средство обнаружения
            self.modifies_flags['capacity'] = 1
                
        if self.parent().radioFacility.isChecked():
            # Радиолучевое средство обнаружения
            self.modifies_flags['radio'] = 1

        if self.parent().irFacility.isChecked():
            # ИК-датчик
            self.modifies_flags['ir'] = 1

        elif self.parent().bombFacility.isChecked():
            # Обнаружитель ВВ
            self.modifies_flags['bomb'] = 1

        if self.parent().warmFacility.isChecked():
            # Тепловой датчик
            self.modifies_flags['warm'] = 1

        if self.parent().gerkonFacility.isChecked():
            # Герконовый датчик
            self.modifies_flags['gerkon'] = 1

        if self.parent().piezoFacility.isChecked():
            # Пьезо датчик
            self.modifies_flags['piezo'] = 1

        if self.parent().metalFacility.isChecked():
            # Металлоискатель
            if self.received_code[0] in (None,1):
                self.modifies_flags['metal'] = 1
            

        #
        # Неподвижные объекты
        #

        #
        if self.parent().turnstileFacility.isChecked():
            # Турникет
            self.received_code[0] = 1
            self.received_code[1] = None

        elif self.parent().gatewayFacility.isChecked():
            # Шлюз
            self.received_code[0] = 2
            self.received_code[1] = None

        elif self.parent().elmechFacility.isChecked():
            # ЭМ замок
            self.received_code[0] = 3
            self.received_code[1] = None

        elif self.parent().wall.isChecked():
            # Стена
            self.received_code[0] = 4
            self.received_code[1] = None
        
        elif self.parent().passage.isChecked():
            # Проход
            self.received_code[0] = 5
            self.received_code[1] = None
            
        elif self.parent().woodDoor.isChecked():
            # Деревянная дверь
            self.received_code[0] = 6
            self.received_code[1] = None          
            current_text = self.parent().woodBox.currentText()
            if current_text == 'Выбивание':
                self.received_code[1] = 1
            elif current_text == 'Разрушение петель':
                self.received_code[1] = 2
            elif current_text == 'Разрушение замка':
                self.received_code[1] = 3
            elif current_text == 'Отжим двери':
                self.received_code[1] = 4
            elif current_text == 'Отжим ригеля':
                self.received_code[1] = 5
            
        elif self.parent().woodMetalDoor.isChecked():
            # Деревянная дверь, обитая металлом
            self.received_code[0] = 7
            self.received_code[1] = None 
            current_text = self.parent().woodMetalBox.currentText()
            if current_text == 'Выбивание':
                self.received_code[1] = 1
            elif current_text == 'Разрушение петель':
                self.received_code[1] = 2
            elif current_text == 'Разрушение замка':
                self.received_code[1] = 3
            elif current_text == 'Отжим двери':
                self.received_code[1] = 4
            elif current_text == 'Отжим ригеля':
                self.received_code[1] = 5

            
        elif self.parent().metalDoor.isChecked():
            # Металлическая дверь
            current_text = self.parent().metalBox.currentText()
            self.received_code[0] = 8
            self.received_code[1] = None
            if current_text == 'Выбивание':
                self.received_code[1] = 1
            elif current_text == 'Разрезание ножовкой':
                self.received_code[1] = 2
            elif current_text == 'Газовая резка':
                self.received_code[1] = 3
            elif current_text == 'Разрушение замка':
                self.received_code[1] = 4
            elif current_text == 'Отжим двери':
                self.received_code[1] = 5
            elif current_text == 'Отжим ригеля':
                self.received_code[1] = 6
            
        elif self.parent().window.isChecked():
            # Окно
            self.received_code[0] = 9
            self.received_code[1] = None
            current_text = self.parent().windowBox.currentText()
            if current_text == 'Пролом стекла А1-А3':
                self.received_code[1] = 1
            elif current_text == 'Пролом стекла Б1':
                self.received_code[1] = 2
            elif current_text == 'Пролом стекла Б2':
                self.received_code[1] = 3
            elif current_text == 'Пролом стекла Б3':
                self.received_code[1] = 4
            
        elif self.parent().concrete.isChecked():
            # Бетонное ограждение
            self.received_code[0] = 10
            self.received_code[1] = None
            current_text = self.parent().concreteBox.currentText()
            if current_text == 'Перелаз':
                self.received_code[1] = 1
            elif current_text == 'Подкоп':
                self.received_code[1] = 2
            
        elif self.parent().concreteAKP.isChecked():
            # Бетонное ограждение c АКП
            self.received_code[0] = 11
            self.received_code[1] = None
            current_text = self.parent().concreteAKPBox.currentText()
            if current_text == 'Перелаз':
                self.received_code[1] = 1
            elif current_text == 'Подкоп':
                self.received_code[1] = 2
            
        elif self.parent().gridWall.isChecked():
            # Сетчатое заграждение
            self.received_code[0] = 12
            self.received_code[1] = None
            current_text = self.parent().gridWallBox.currentText()
            if current_text == 'Перелаз':
                self.received_code[1] = 1
            elif current_text == 'Пролом':
                self.received_code[1] = 2
            elif current_text == 'Подкоп':
                self.received_code[1] = 3
            
        elif self.parent().barbedWall.isChecked():
            # Колючая проволока
            self.received_code[0] = 13
            self.received_code[1] = None
            current_text = self.parent().barbedWallBox.currentText()
            if current_text == 'Перелаз':
                self.received_code[1] = 1
            elif current_text == 'Пролом':
                self.received_code[1] = 2
            elif current_text == 'Подкоп':
                self.received_code[1] = 3
        
        elif self.parent().antiram.isChecked():
            # Противотаранное устройство
            self.received_code[0] = 14
            self.received_code[1] = None
            

        #
        # Передвижные объекты
        #
        elif self.parent().intruder.isChecked():
            # Нарушитель
            self.received_code[0] = 15
            self.received_code[1] = None
            
        elif self.parent().PFZ.isChecked():
            # ПФЗ
            self.received_code[0] = 16
            self.received_code[1] = None
            
        elif self.parent().startTG.isChecked():
            # Начальная точка тревожной группы
            self.received_code[0] = 17
            self.received_code[1] = None
            
        elif self.parent().endTG.isChecked():
            # Конечная точка тревожной группы
            self.received_code[0] = 18
            self.received_code[1] = None

        #
        #
        elif self.parent().clearCellButton.isChecked():
            # Очистка клеток
            self.received_code[0] = 0
            self.received_code[1] = None
        
        self.cellProcess(self.received_code)
        

    # Отрисовка клетки
    def cellProcess(self, received_code):


        self.detect_prob = 1
        #
        # Средства обнаружения (модификаторы)
        #
        
        # Видеокамера
        if self.modifies_flags['video']:
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('brown', 1)

        # Датчик разбития стекла
        if self.modifies_flags['glass']:
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('blue', 1)
                
        # Емкостное средство обнаружения
        if  self.modifies_flags['capacity']:
            self.detect_prob *= self.detect_prob*(1-0.9)
            self.drawFacility('red', 1)
                
        # Радиолучевое средство обнаружения
        if self.modifies_flags['radio']:
            self.modifies_flags['radio'] = 1
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('brown', 2)

        # ИК-датчик
        if self.modifies_flags['ir']:
            self.detect_prob *= self.detect_prob*(1-1)
            self.drawFacility('blue', 2)

        # Обнаружитель ВВ
        if self.modifies_flags['bomb']:
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('red', 2)

        # Тепловой датчик
        if self.modifies_flags['warm']:
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('brown', 3)

            # Герконовый датчик
        if self.modifies_flags['gerkon']:
            self.detect_prob *= self.detect_prob*(1-1)
            self.drawFacility('blue', 3)

        # Пьезо датчик
        if self.modifies_flags['piezo']:
            self.detect_prob *= self.detect_prob*(1-0.95)
            self.drawFacility('red', 3)

        # Металлоискатель
        
        if self.modifies_flags['metal']:
            if super().parent().intruder_have[2] == 0:
                self.detect_prob = self.detect_prob*(1-1)

            facility_indicator = QPushButton(self)
            facility_indicator.move(2,2)
            facility_indicator.resize(10,10)
            facility_indicator.setStyleSheet('''QPushButton {background-image: url(pictures/MeFinder.png);
                        border-radius: 1px;background-color: rgba(255,255,255,0); border-color: black; border-radius: 5}''')
            facility_indicator.clicked.connect(self.click)
            facility_indicator.show()
            facility_indicator.raise_()
            self.modifies.append(facility_indicator)
       

        # Чтобы не оставлять лишние клетки с подкопом и турникетом
        if 1 not in self.modifies_flags.values():
            if (self.x, self.y) in self.parent().diggings:
                self.parent().diggings.remove((self.x, self.y))
            if received_code[0] != 1:
                self.setText('')
        
        #
        # Неподвижные объекты
        #

        #
        if received_code[0] == 1:
            # Турникет
            self.style = 'QPushButton {background-color: white; color:black; border-color:  white; border-radius: 5}'
            self.cost = [-1*super().parent().intruder_have[1],6,0]
            self.setText('T')

        elif received_code[0] == 2:
            # Шлюз
            self.style = 'QPushButton {background-color: white; color:black; border-color:  white; border-radius: 5}'
            self.cost = [-1*super().parent().intruder_have[1],6,0]
            self.setText('Ш')

        elif received_code[0] == 3:
            # ЭМ замок
            self.style = 'QPushButton {background-color: white; color:black; border-color:  white; border-radius: 5}'
            self.cost = [-1,6,0]
            self.setText('L')

        elif received_code[0] == 4:
            # Стена
            self.style = 'QPushButton {background-image: url(pictures/WallPic.png); border-color:  black; border-radius: 5}'
            self.cost = [4,-1,4]

        
        elif received_code[0] == 5:
            # Проход
            self.style = 'QPushButton {background-image: url(pictures/EntryPic.png); border-color:  black; border-radius: 5}'
            self.cost = [3,6,3]
            
        elif received_code[0] == 6:
            # Деревянная дверь        
            if received_code[1] == 1:
                self.cost = [15,6,3]
            elif received_code[1] == 2:
                self.cost = [60,6,3]
            elif received_code[1] == 3:
                self.cost = [180,6,3]
            elif received_code[1] == 4:
                self.cost = [145,6,3]
            elif received_code[1] == 5:
                self.cost = [195,6,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/WDoorPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 7:
            # Деревянная дверь, обитая металлом
            current_text = self.parent().woodMetalBox.currentText()
            if received_code[1] == 1:
                self.cost = [40,6,3]
            elif received_code[1] == 2:
                self.cost = [60,6,3]
            elif received_code[1] == 3:
                self.cost = [180,6,3]
            elif received_code[1] == 4:
                self.cost = [145,6,3]
            elif received_code[1] == 5:
                self.cost = [195,6,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/WMeDoorPic.png); border-color:  black; border-radius: 5}'

            
        elif received_code[0] == 8:
            # Металлическая дверь
            if received_code[1] == 1:
                self.cost = [40,6,3]
            elif received_code[1] == 2:
                self.cost = [40,6,3]
            elif received_code[1] == 3:
                self.cost = [60,6,3]
            elif received_code[1] == 4:
                self.cost = [180,6,3]
            elif received_code[1] == 5:
                self.cost = [145,6,3]
            elif received_code[1] == 6:
                self.cost = [195,6,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/MeDoorPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 9:
            # Окно
            if received_code[1] == 1:
                self.cost = [5,-1,3]
            elif received_code[1] == 2:
                self.cost = [90,-1,3]
            elif received_code[1] == 3:
                self.cost = [130,-1,3]
            elif received_code[1] == 4:
                self.cost = [140,-1,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/WindowPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 10:
            # Бетонное ограждение
            if received_code[1] == 1:
                self.cost = [5,-1,5]
            elif received_code[1] == 2:
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/BarrPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 11:
            # Бетонное ограждение c АКП
            if received_code[1] == 1:
                self.cost = [5,-1,5]
            elif received_code[1] == 2:
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/BarrAKLPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 12:
            # Сетчатое заграждение
            if received_code[1] == 1:
                self.cost = [5,-1,5]
            elif received_code[1] == 2:
                self.cost = [6*super().parent().intruder_have[0],-1,3]
            elif received_code[1] == 3:
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/BarrChainPic.png); border-color:  black; border-radius: 5}'
            
        elif received_code[0] == 13:
            # Колючая проволока
            if received_code[1] == 1:
                self.cost = [7,-1,5]
            elif received_code[1] == 2:
                self.cost = [7,-1,3]
            elif received_code[1] == 3:
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if received_code[1]:
                self.style = 'QPushButton {background-image: url(pictures/AKLPic.png); border-color:  black; border-radius: 5}'

        elif received_code[0] == 14:
            # Противотаранное устройство
            self.style = 'QPushButton {background-color: purple; color:black; border-color:  white; border-radius: 5}'
            self.cost = [-1,-1,-1]
            
        #
        # Передвижные объекты
        #
        elif received_code[0] == 15:
            # Нарушитель
            self.style = 'QPushButton {background-color: red; border-color:  black; border-radius: 5}'
            if (self.x, self.y) not in super().parent().intruders:
                super().parent().intruders.append((self.x, self.y))
            
        elif received_code[0] == 16:
            # ПФЗ
            received_code[1] = None
            self.style = 'QPushButton {background-color: green; border-color:  black; border-radius: 5}'
            if (self.x, self.y) not in super().parent().PFZs:
                super().parent().PFZs.append((self.x, self.y))
            
        elif received_code[0] == 17:
            # Начальная точка тревожной группы
            if super().parent().startTG_coordinate != None:
                super().parent().field[super().parent().startTG_coordinate[1]][super().parent().startTG_coordinate[0]].setStyleSheet(self.default_style)
            self.style = 'QPushButton {background-color: lightblue; border-color:  black; border-radius: 5}'
            super().parent().startTG_coordinate = (self.x, self.y)
            
        elif received_code[0] == 18:
            # Конечная точка тревожной группы
            if super().parent().endTG_coordinate != None:
                super().parent().field[super().parent().endTG_coordinate[1]][super().parent().endTG_coordinate[0]].setStyleSheet(self.default_style)
            self.style = 'QPushButton {background-color: darkblue; border-color:  black; border-radius: 5}'
            super().parent().endTG_coordinate = (self.x, self.y)

        #
        #
        elif received_code[0] == 0:
            # Очистка клеток
            self.style = self.default_style
            for key in self.modifies_flags:
                self.modifies_flags[key] = 0
            # Удаляем клетку из всех массивов хранения
            for array in (super().parent().intruders, super().parent().PFZs,):
                if (self.x,self.y) in array:
                    array.remove((self.x,self.y))
            # Тревожную группы возвращаем в начальное значение
            if super().parent().startTG_coordinate == (self.x, self.y):
                super().parent().startTG_coordinate = None
            elif super().parent().endTG_coordinate == (self.x, self.y):
                super().parent().endTG_coordinate = None

            # Убираем средства обнаружения
            while len(self.modifies) > 0:
                self.modifies[-1].setParent(None)
                self.modifies.remove(self.modifies[-1])
            
            self.cost = [0,0,0]
            self.detect_prob = 1
            self.setText('')
                
        super().setStyleSheet(self.style)
    
    # Отрисовка средств обнаружения
    def drawFacility(self,color,margin):
        facility_indicator = QPushButton(self)
        facility_indicator.move(margin,margin)
        facility_indicator.resize(13-margin*2,13-margin*2)
        facility_indicator.setStyleSheet('''QPushButton {
            border: 1px solid '''+ color + ''';
            border-radius: 1px;
            background-color: rgba(255,255,255,0);
            }'''
        )
        facility_indicator.clicked.connect(self.click)
        
        # Вынесение на передний план
        facility_indicator.show()
        facility_indicator.raise_()

        # Сложить в массив, чтобы потом можно было удалить
        self.modifies.append(facility_indicator)

