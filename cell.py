from PyQt5.QtWidgets import QPushButton

# Класс клетки на поле 
class Cell(QPushButton):
    def __init__(self, parent, x, y):
        super(Cell, self).__init__(parent)
        self.resize(15,15)

        # Свойства ячейки
        # На путь между клетками тратится 3 сек
        self.cost = [0,6,0] # Первое число для нарушителя, второе -- для ТГ, третье -- для движения ТГ по следам нарушителя
        self.x = x
        self.y = y

        # Наличие модификаторов
        self.capacity_flag = False
        self.radio_flag = False
        self.modifies = []
        # Шанс необнаружения
        self.detect_prob = 1

        # CSS стиль ячейки
        self.default_style = 'QPushButton {background-color: rgb(210,210,210); border-color:  black; border-radius: 5}'
        self.style = self.default_style
        self.setStyleSheet(self.default_style)


    def click(self):
        # 
        # Стоимость подкопов расчитывается в основном файле
        #
        
        #
        # Средства обнаружения (модификаторы)
        #
        if self.parent().capacityFacility.isChecked():
            # Емкостное средство обнаружения
            if not self.capacity_flag:
                self.capacity_flag = True
                self.detect_prob *= self.detect_prob*(1-0.9)
                self.drawFacility('red', 1)
                
        elif self.parent().radioFacility.isChecked():
            # Радиолучевое средство обнаружения
            if not self.radio_flag:
                self.radio_flag = True
                self.detect_prob *= self.detect_prob*(1-0.95)
                self.drawFacility('blue', 2)

        
        # Чтобы не оставлять лишние клетки с подкопом
        if (not self.capacity_flag) and (not self.radio_flag):
            if (self.x, self.y) in self.parent().diggings:
                self.parent().diggings.remove((self.x, self.y))
        
        #
        # Неподвижные объекты
        #
        if self.parent().wall.isChecked():
            # Стена
            self.style = 'QPushButton {background-image: url(pictures/WallPic.png); border-color:  black; border-radius: 5}'
            self.cost = [4,-1,4]
            self.checkFacilities()
            
        
        elif self.parent().passage.isChecked():
            # Проход
            self.style = 'QPushButton {background-image: url(pictures/EntryPic.png); border-color:  black; border-radius: 5}'
            self.cost = [3,6,3]
            self.checkFacilities()
            
        elif self.parent().woodDoor.isChecked():
            # Деревянная дверь
            
            current_text = self.parent().woodBox.currentText()
            if current_text == 'Выбивание':
                self.cost = [15,6,3]
            elif current_text == 'Разрушение петель':
                self.cost = [60,6,3]
            elif current_text == 'Разрушение замка':
                self.cost = [180,6,3]
            elif current_text == 'Отжим двери':
                self.cost = [145,6,3]
            elif currcurrent_textentText == 'Отжим ригеля':
                self.cost = [195,6,3]
            if current_text != '':
                self.checkFacilities()
                self.style = 'QPushButton {background-image: url(pictures/WDoorPic.png); border-color:  black; border-radius: 5}'
            
        elif self.parent().woodMetalDoor.isChecked():
            # Деревянная дверь, обитая металлом
            
            current_text = self.parent().woodMetalBox.currentText()
            if current_text == 'Выбивание':
                self.cost = [40,6,3]
            elif current_text == 'Разрушение петель':
                self.cost = [60,6,3]
            elif current_text == 'Разрушение замка':
                self.cost = [180,6,3]
            elif current_text == 'Отжим двери':
                self.cost = [145,6,3]
            elif current_text == 'Отжим ригеля':
                self.cost = [195,6,3]
            if current_text != '':
                self.checkFacilities()
                self.style = 'QPushButton {background-image: url(pictures/WMeDoorPic.png); border-color:  black; border-radius: 5}'

            
        elif self.parent().metalDoor.isChecked():
            # Металлическая дверь
            
            current_text = self.parent().metalBox.currentText()
            if current_text == 'Выбивание':
                self.cost = [40,6,3]
            elif current_text == 'Разрезание ножовкой':
                self.cost = [40,6,3]
            elif current_text == 'Газовая резка':
                self.cost = [60,6,3]
            elif current_text == 'Разрушение замка':
                self.cost = [180,6,3]
            elif current_text == 'Отжим двери':
                self.cost = [145,6,3]
            elif current_text == 'Отжим ригеля':
                self.cost = [195,6,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/MeDoorPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        elif self.parent().window.isChecked():
            # Окно
            
            current_text = self.parent().window.textIndex()
            if current_text == 'Пролом стекла А1-А3':
                self.cost = [5,-1,3]
            elif current_text == 'Пролом стекла Б1':
                self.cost = [90,-1,3]
            elif current_text == 'Пролом стекла Б2':
                self.cost = [130,-1,3]
            elif current_text == 'Пролом стекла Б3':
                self.cost = [140,-1,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/WindowPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        elif self.parent().concrete.isChecked():
            # Бетонное ограждение
            
            current_text = self.parent().concreteBox.currentText()
            if current_text == 'Перелаз':
                self.cost = [5,-1,5]
            elif current_text == 'Подкоп':
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/BarrPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        elif self.parent().concreteAKP.isChecked():
            # Бетонное ограждение c АКП
            
            current_text = self.parent().concreteAKPBox.currentText()
            if current_text == 'Перелаз':
                self.cost = [5,-1,5]
            elif current_text == 'Подкоп':
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/BarrAKLPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        elif self.parent().gridWall.isChecked():
            # Сетчатое заграждение
            
            current_text = self.parent().gridWallBox.currentText()
            if current_text == 'Перелаз':
                self.cost = [5,-1,5]
            elif current_text == 'Пролом':
                self.cost = [6,-1,3]
            elif current_text == 'Подкоп':
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/BarrChainPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        elif self.parent().barbedWall.isChecked():
            # Колючая проволока
            
            current_text = self.parent().barbedWallBox.currentText()
            if current_text == 'Перелаз':
                self.cost = [7,-1,5]
            elif current_text == 'Пролом':
                self.cost = [7,-1,3]
            elif current_text == 'Подкоп':
                self.parent().diggings.append((self.x, self.y))
                self.cost = [None,-1,3]
            if current_text != '':
                self.style = 'QPushButton {background-image: url(pictures/AKLPic.png); border-color:  black; border-radius: 5}'
                self.checkFacilities()
            
        #
        # Передвижные объекты
        #
        elif self.parent().intruder.isChecked():
            # Нарушитель

            self.style = 'QPushButton {background-color: red; border-color:  black; border-radius: 5}'
            if (self.x, self.y) not in super().parent().intruders:
                super().parent().intruders.append((self.x, self.y))
            
        elif self.parent().PFZ.isChecked():
            # ПФЗ

            self.style = 'QPushButton {background-color: green; border-color:  black; border-radius: 5}'
            if (self.x, self.y) not in super().parent().PFZs:
                super().parent().PFZs.append((self.x, self.y))
            
        elif self.parent().startTG.isChecked():
            # Начальная точка тревожной группы

            if super().parent().startTG_coordinate != None:
                super().parent().field[super().parent().startTG_coordinate[1]][super().parent().startTG_coordinate[0]].setStyleSheet(self.default_style)
            self.style = 'QPushButton {background-color: lightblue; border-color:  black; border-radius: 5}'
            super().parent().startTG_coordinate = (self.x, self.y)
            
        elif self.parent().endTG.isChecked():
            # Конечная точка тревожной группы
            
            if super().parent().endTG_coordinate != None:
                super().parent().field[super().parent().endTG_coordinate[1]][super().parent().endTG_coordinate[0]].setStyleSheet(self.default_style)
            self.style = 'QPushButton {background-color: darkblue; border-color:  black; border-radius: 5}'
            super().parent().endTG_coordinate = (self.x, self.y)

        #
        #
        elif self.parent().clearCellButton.isChecked():
            # Очистка клеток

            self.style = self.default_style
            self.capacity_flag = False
            self.radio_flag = False
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
            for facility in self.modifies:
                facility.setParent(None)
                self.modifies.remove(facility)
            
            self.cost = [0,6,0]
            self.detect_prob = 1
                



        super().setStyleSheet(self.style)
    
    # Отрисовка средств обнаружения
    def drawFacility(self,color,margin):
        facility_indicator = QPushButton(self)
        facility_indicator.move(margin,margin)
        facility_indicator.resize(15-margin*2,15-margin*2)
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

    def checkFacilities(self):
        if self.capacity_flag:
            self.cost[0] += 1
        if self.radio_flag:
            self.cost[0] += 1
