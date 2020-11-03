# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.actionButton = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton.setGeometry(QtCore.QRect(730, 680, 81, 41))
        self.actionButton.setObjectName("actionButton")
        self.groundBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groundBox.setGeometry(QtCore.QRect(730, 10, 461, 80))
        self.groundBox.setObjectName("groundBox")
        self.freezeBox = QtWidgets.QCheckBox(self.groundBox)
        self.freezeBox.setGeometry(QtCore.QRect(190, 30, 88, 31))
        self.freezeBox.setObjectName("freezeBox")
        self.chooseGroundBox = QtWidgets.QComboBox(self.groundBox)
        self.chooseGroundBox.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.chooseGroundBox.setObjectName("chooseGroundBox")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.chooseGroundBox.addItem("")
        self.helpGroundButton = QtWidgets.QPushButton(self.groundBox)
        self.helpGroundButton.setGeometry(QtCore.QRect(360, 30, 88, 31))
        icon = QtGui.QIcon.fromTheme("help-about")
        self.helpGroundButton.setIcon(icon)
        self.helpGroundButton.setObjectName("helpGroundButton")
        self.facilitiesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.facilitiesBox.setGeometry(QtCore.QRect(730, 100, 461, 301))
        self.facilitiesBox.setTitle("")
        self.facilitiesBox.setObjectName("facilitiesBox")
        self.stackedWidget = QtWidgets.QStackedWidget(self.facilitiesBox)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 441, 271))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.woodDoor = QtWidgets.QRadioButton(self.page_1)
        self.woodDoor.setGeometry(QtCore.QRect(10, 50, 181, 22))
        self.woodDoor.setObjectName("woodDoor")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.woodDoor)
        self.woodMetalDoor = QtWidgets.QRadioButton(self.page_1)
        self.woodMetalDoor.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.woodMetalDoor.setObjectName("woodMetalDoor")
        self.buttonGroup.addButton(self.woodMetalDoor)
        self.metalDoor = QtWidgets.QRadioButton(self.page_1)
        self.metalDoor.setGeometry(QtCore.QRect(10, 180, 191, 22))
        self.metalDoor.setObjectName("metalDoor")
        self.buttonGroup.addButton(self.metalDoor)
        self.window = QtWidgets.QRadioButton(self.page_1)
        self.window.setGeometry(QtCore.QRect(10, 240, 105, 22))
        self.window.setObjectName("window")
        self.buttonGroup.addButton(self.window)
        self.woodBox = QtWidgets.QComboBox(self.page_1)
        self.woodBox.setGeometry(QtCore.QRect(250, 50, 171, 31))
        self.woodBox.setObjectName("woodBox")
        self.woodBox.addItem("")
        self.woodBox.addItem("")
        self.woodBox.addItem("")
        self.woodBox.addItem("")
        self.woodBox.addItem("")
        self.woodMetalBox = QtWidgets.QComboBox(self.page_1)
        self.woodMetalBox.setGeometry(QtCore.QRect(250, 110, 171, 31))
        self.woodMetalBox.setObjectName("woodMetalBox")
        self.woodMetalBox.addItem("")
        self.woodMetalBox.addItem("")
        self.woodMetalBox.addItem("")
        self.woodMetalBox.addItem("")
        self.woodMetalBox.addItem("")
        self.metalBox = QtWidgets.QComboBox(self.page_1)
        self.metalBox.setGeometry(QtCore.QRect(250, 170, 171, 31))
        self.metalBox.setObjectName("metalBox")
        self.metalBox.addItem("")
        self.metalBox.addItem("")
        self.metalBox.addItem("")
        self.metalBox.addItem("")
        self.metalBox.addItem("")
        self.metalBox.addItem("")
        self.windowBox = QtWidgets.QComboBox(self.page_1)
        self.windowBox.setGeometry(QtCore.QRect(250, 230, 171, 31))
        self.windowBox.setObjectName("windowBox")
        self.windowBox.addItem("")
        self.windowBox.addItem("")
        self.windowBox.addItem("")
        self.windowBox.addItem("")
        self.tacticsLabel_1 = QtWidgets.QLabel(self.page_1)
        self.tacticsLabel_1.setGeometry(QtCore.QRect(260, 10, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tacticsLabel_1.setFont(font)
        self.tacticsLabel_1.setObjectName("tacticsLabel_1")
        self.facilitiesLabel_1 = QtWidgets.QLabel(self.page_1)
        self.facilitiesLabel_1.setGeometry(QtCore.QRect(20, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.facilitiesLabel_1.setFont(font)
        self.facilitiesLabel_1.setObjectName("facilitiesLabel_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.concrete = QtWidgets.QRadioButton(self.page_2)
        self.concrete.setGeometry(QtCore.QRect(10, 50, 191, 22))
        self.concrete.setObjectName("concrete")
        self.buttonGroup.addButton(self.concrete)
        self.concreteAKP = QtWidgets.QRadioButton(self.page_2)
        self.concreteAKP.setGeometry(QtCore.QRect(10, 80, 171, 51))
        self.concreteAKP.setText("Бетонное\n"
"ограждение с\n"
"козырьком из АКП ")
        self.concreteAKP.setObjectName("concreteAKP")
        self.buttonGroup.addButton(self.concreteAKP)
        self.gridWall = QtWidgets.QRadioButton(self.page_2)
        self.gridWall.setGeometry(QtCore.QRect(10, 160, 201, 22))
        self.gridWall.setObjectName("gridWall")
        self.buttonGroup.addButton(self.gridWall)
        self.barbedWall = QtWidgets.QRadioButton(self.page_2)
        self.barbedWall.setGeometry(QtCore.QRect(10, 200, 171, 22))
        self.barbedWall.setObjectName("barbedWall")
        self.buttonGroup.addButton(self.barbedWall)
        self.concreteAKPBox = QtWidgets.QComboBox(self.page_2)
        self.concreteAKPBox.setGeometry(QtCore.QRect(250, 100, 171, 31))
        self.concreteAKPBox.setObjectName("concreteAKPBox")
        self.concreteAKPBox.addItem("")
        self.concreteAKPBox.addItem("")
        self.concreteBox = QtWidgets.QComboBox(self.page_2)
        self.concreteBox.setGeometry(QtCore.QRect(250, 50, 171, 31))
        self.concreteBox.setObjectName("concreteBox")
        self.concreteBox.addItem("")
        self.concreteBox.addItem("")
        self.gridWallBox = QtWidgets.QComboBox(self.page_2)
        self.gridWallBox.setGeometry(QtCore.QRect(250, 150, 171, 31))
        self.gridWallBox.setObjectName("gridWallBox")
        self.gridWallBox.addItem("")
        self.gridWallBox.addItem("")
        self.gridWallBox.addItem("")
        self.barbedWallBox = QtWidgets.QComboBox(self.page_2)
        self.barbedWallBox.setGeometry(QtCore.QRect(250, 190, 171, 31))
        self.barbedWallBox.setObjectName("barbedWallBox")
        self.barbedWallBox.addItem("")
        self.barbedWallBox.addItem("")
        self.barbedWallBox.addItem("")
        self.facilitiesLabel_2 = QtWidgets.QLabel(self.page_2)
        self.facilitiesLabel_2.setGeometry(QtCore.QRect(20, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.facilitiesLabel_2.setFont(font)
        self.facilitiesLabel_2.setObjectName("facilitiesLabel_2")
        self.tacticsLabel_2 = QtWidgets.QLabel(self.page_2)
        self.tacticsLabel_2.setGeometry(QtCore.QRect(260, 10, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tacticsLabel_2.setFont(font)
        self.tacticsLabel_2.setObjectName("tacticsLabel_2")
        self.antiram = QtWidgets.QRadioButton(self.page_2)
        self.antiram.setGeometry(QtCore.QRect(10, 240, 191, 22))
        self.antiram.setObjectName("antiram")
        self.buttonGroup.addButton(self.antiram)
        self.gridWallBox.raise_()
        self.concrete.raise_()
        self.concreteAKP.raise_()
        self.gridWall.raise_()
        self.barbedWall.raise_()
        self.concreteAKPBox.raise_()
        self.concreteBox.raise_()
        self.barbedWallBox.raise_()
        self.facilitiesLabel_2.raise_()
        self.tacticsLabel_2.raise_()
        self.antiram.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.irFacility = QtWidgets.QRadioButton(self.page_3)
        self.irFacility.setGeometry(QtCore.QRect(20, 100, 171, 22))
        self.irFacility.setObjectName("irFacility")
        self.buttonGroup.addButton(self.irFacility)
        self.gerkonFacility = QtWidgets.QRadioButton(self.page_3)
        self.gerkonFacility.setGeometry(QtCore.QRect(250, 100, 191, 22))
        self.gerkonFacility.setObjectName("gerkonFacility")
        self.buttonGroup.addButton(self.gerkonFacility)
        self.elmechFacility = QtWidgets.QRadioButton(self.page_3)
        self.elmechFacility.setGeometry(QtCore.QRect(20, 160, 211, 22))
        self.elmechFacility.setObjectName("elmechFacility")
        self.buttonGroup.addButton(self.elmechFacility)
        self.turnstileFacility = QtWidgets.QRadioButton(self.page_3)
        self.turnstileFacility.setGeometry(QtCore.QRect(20, 40, 151, 22))
        self.turnstileFacility.setObjectName("turnstileFacility")
        self.buttonGroup.addButton(self.turnstileFacility)
        self.tacticsLabel_3 = QtWidgets.QLabel(self.page_3)
        self.tacticsLabel_3.setGeometry(QtCore.QRect(110, 10, 251, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tacticsLabel_3.setFont(font)
        self.tacticsLabel_3.setObjectName("tacticsLabel_3")
        self.videoFacility = QtWidgets.QRadioButton(self.page_3)
        self.videoFacility.setGeometry(QtCore.QRect(20, 70, 151, 22))
        self.videoFacility.setObjectName("videoFacility")
        self.buttonGroup.addButton(self.videoFacility)
        self.cardFacility = QtWidgets.QRadioButton(self.page_3)
        self.cardFacility.setGeometry(QtCore.QRect(20, 190, 191, 22))
        self.cardFacility.setObjectName("cardFacility")
        self.buttonGroup.addButton(self.cardFacility)
        self.alarmFacility = QtWidgets.QRadioButton(self.page_3)
        self.alarmFacility.setGeometry(QtCore.QRect(250, 190, 191, 22))
        self.alarmFacility.setObjectName("alarmFacility")
        self.buttonGroup.addButton(self.alarmFacility)
        self.glassFacility = QtWidgets.QRadioButton(self.page_3)
        self.glassFacility.setGeometry(QtCore.QRect(250, 40, 191, 22))
        self.glassFacility.setObjectName("glassFacility")
        self.buttonGroup.addButton(self.glassFacility)
        self.warmFacility = QtWidgets.QRadioButton(self.page_3)
        self.warmFacility.setGeometry(QtCore.QRect(250, 70, 191, 22))
        self.warmFacility.setObjectName("warmFacility")
        self.buttonGroup.addButton(self.warmFacility)
        self.bioFacility = QtWidgets.QRadioButton(self.page_3)
        self.bioFacility.setGeometry(QtCore.QRect(20, 130, 221, 22))
        self.bioFacility.setObjectName("bioFacility")
        self.buttonGroup.addButton(self.bioFacility)
        self.capacityFacility = QtWidgets.QRadioButton(self.page_3)
        self.capacityFacility.setGeometry(QtCore.QRect(250, 130, 181, 21))
        self.capacityFacility.setObjectName("capacityFacility")
        self.buttonGroup.addButton(self.capacityFacility)
        self.radioFacility = QtWidgets.QRadioButton(self.page_3)
        self.radioFacility.setGeometry(QtCore.QRect(250, 160, 201, 20))
        self.radioFacility.setObjectName("radioFacility")
        self.buttonGroup.addButton(self.radioFacility)
        self.bombFacility = QtWidgets.QRadioButton(self.page_3)
        self.bombFacility.setGeometry(QtCore.QRect(20, 220, 151, 22))
        self.bombFacility.setObjectName("bombFacility")
        self.buttonGroup.addButton(self.bombFacility)
        self.piezoFacility = QtWidgets.QRadioButton(self.page_3)
        self.piezoFacility.setGeometry(QtCore.QRect(250, 220, 181, 22))
        self.piezoFacility.setObjectName("piezoFacility")
        self.buttonGroup.addButton(self.piezoFacility)
        self.stackedWidget.addWidget(self.page_3)
        self.listButton_next = QtWidgets.QPushButton(self.facilitiesBox)
        self.listButton_next.setGeometry(QtCore.QRect(440, 10, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listButton_next.setFont(font)
        self.listButton_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listButton_next.setStyleSheet("QPushButton {border:  none}")
        self.listButton_next.setText("")
        icon = QtGui.QIcon.fromTheme("go-next")
        self.listButton_next.setIcon(icon)
        self.listButton_next.setObjectName("listButton_next")
        self.listButton_prev = QtWidgets.QPushButton(self.facilitiesBox)
        self.listButton_prev.setGeometry(QtCore.QRect(420, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listButton_prev.setFont(font)
        self.listButton_prev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listButton_prev.setStyleSheet("QPushButton {border:  none}")
        self.listButton_prev.setText("")
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.listButton_prev.setIcon(icon)
        self.listButton_prev.setObjectName("listButton_prev")
        self.tacticsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.tacticsBox.setGeometry(QtCore.QRect(730, 460, 461, 111))
        self.tacticsBox.setObjectName("tacticsBox")
        self.consistentTactic = QtWidgets.QRadioButton(self.tacticsBox)
        self.consistentTactic.setEnabled(True)
        self.consistentTactic.setGeometry(QtCore.QRect(30, 30, 361, 21))
        self.consistentTactic.setChecked(True)
        self.consistentTactic.setObjectName("consistentTactic")
        self.intermediateTactic = QtWidgets.QRadioButton(self.tacticsBox)
        self.intermediateTactic.setGeometry(QtCore.QRect(30, 50, 321, 51))
        self.intermediateTactic.setObjectName("intermediateTactic")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(730, 580, 461, 91))
        self.groupBox.setObjectName("groupBox")
        self.intruder = QtWidgets.QRadioButton(self.groupBox)
        self.intruder.setGeometry(QtCore.QRect(30, 30, 201, 22))
        self.intruder.setObjectName("intruder")
        self.buttonGroup.addButton(self.intruder)
        self.PFZ = QtWidgets.QRadioButton(self.groupBox)
        self.PFZ.setGeometry(QtCore.QRect(30, 60, 181, 22))
        self.PFZ.setObjectName("PFZ")
        self.buttonGroup.addButton(self.PFZ)
        self.startTG = QtWidgets.QRadioButton(self.groupBox)
        self.startTG.setGeometry(QtCore.QRect(260, 30, 211, 22))
        self.startTG.setObjectName("startTG")
        self.buttonGroup.addButton(self.startTG)
        self.endTG = QtWidgets.QRadioButton(self.groupBox)
        self.endTG.setGeometry(QtCore.QRect(260, 60, 201, 22))
        self.endTG.setObjectName("endTG")
        self.buttonGroup.addButton(self.endTG)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(730, 410, 461, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.wall = QtWidgets.QRadioButton(self.groupBox_2)
        self.wall.setGeometry(QtCore.QRect(30, 10, 105, 22))
        self.wall.setObjectName("wall")
        self.buttonGroup.addButton(self.wall)
        self.passage = QtWidgets.QRadioButton(self.groupBox_2)
        self.passage.setGeometry(QtCore.QRect(260, 10, 105, 22))
        self.passage.setObjectName("passage")
        self.buttonGroup.addButton(self.passage)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(730, 730, 121, 41))
        self.clearButton.setObjectName("clearButton")
        self.clearCellButton = QtWidgets.QRadioButton(self.centralwidget)
        self.clearCellButton.setGeometry(QtCore.QRect(820, 680, 31, 41))
        self.clearCellButton.setStyleSheet("QRadioButton::indicator {\n"
"     width: 30px;\n"
"     height: 30px;\n"
" }\n"
"QRadioButton::indicator::unchecked {\n"
"     image: url(pictures/ClearPicUnchecked.png);\n"
" }\n"
"QRadioButton::indicator::checked {\n"
"     image: url(pictures/ClearPicChecked.png);\n"
" }")
        self.clearCellButton.setText("")
        self.clearCellButton.setObjectName("clearCellButton")
        self.buttonGroup.addButton(self.clearCellButton)
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(910, 680, 281, 91))
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.saveButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QtCore.QSize(24, 24))
        self.saveButton.setObjectName("saveButton")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(30, 0, 31, 31))
        self.loadButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pictures/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadButton.setIcon(icon1)
        self.loadButton.setIconSize(QtCore.QSize(24, 24))
        self.loadButton.setObjectName("loadButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chooseGroundBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.woodBox.setCurrentIndex(-1)
        self.woodMetalBox.setCurrentIndex(-1)
        self.metalBox.setCurrentIndex(-1)
        self.windowBox.setCurrentIndex(-1)
        self.concreteAKPBox.setCurrentIndex(-1)
        self.concreteBox.setCurrentIndex(-1)
        self.gridWallBox.setCurrentIndex(-1)
        self.barbedWallBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.actionButton, self.freezeBox)
        MainWindow.setTabOrder(self.freezeBox, self.chooseGroundBox)
        MainWindow.setTabOrder(self.chooseGroundBox, self.helpGroundButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionButton.setText(_translate("MainWindow", "Расчет"))
        self.groundBox.setTitle(_translate("MainWindow", "Тип почвы"))
        self.freezeBox.setText(_translate("MainWindow", "Мерзлый"))
        self.chooseGroundBox.setItemText(0, _translate("MainWindow", "Слабый грунт тип 1"))
        self.chooseGroundBox.setItemText(1, _translate("MainWindow", "Слабый грунт тип 2"))
        self.chooseGroundBox.setItemText(2, _translate("MainWindow", "Средний грунт тип 1"))
        self.chooseGroundBox.setItemText(3, _translate("MainWindow", "Средний грунт тип 2"))
        self.chooseGroundBox.setItemText(4, _translate("MainWindow", "Твердый грунт тип 1"))
        self.chooseGroundBox.setItemText(5, _translate("MainWindow", "Твердый грунт тип 2"))
        self.chooseGroundBox.setItemText(6, _translate("MainWindow", "Скальный грунт тип 1"))
        self.chooseGroundBox.setItemText(7, _translate("MainWindow", "Скальный грунт тип 2"))
        self.chooseGroundBox.setItemText(8, _translate("MainWindow", "Скальный грунт тип 3"))
        self.helpGroundButton.setText(_translate("MainWindow", "Справка"))
        self.woodDoor.setText(_translate("MainWindow", "Деревянная дверь"))
        self.woodMetalDoor.setText(_translate("MainWindow", "Деревянная дверь,\n"
"обитая металлом"))
        self.metalDoor.setText(_translate("MainWindow", "Металлическая дверь"))
        self.window.setText(_translate("MainWindow", "Окно"))
        self.woodBox.setItemText(0, _translate("MainWindow", "Выбивание"))
        self.woodBox.setItemText(1, _translate("MainWindow", "Разрушение петель "))
        self.woodBox.setItemText(2, _translate("MainWindow", "Разрушение замка"))
        self.woodBox.setItemText(3, _translate("MainWindow", "Отжим двери"))
        self.woodBox.setItemText(4, _translate("MainWindow", "Отжим ригеля"))
        self.woodMetalBox.setItemText(0, _translate("MainWindow", "Выбивание"))
        self.woodMetalBox.setItemText(1, _translate("MainWindow", "Разрушение петель"))
        self.woodMetalBox.setItemText(2, _translate("MainWindow", "Разрушенеие замка"))
        self.woodMetalBox.setItemText(3, _translate("MainWindow", "Отжим двери"))
        self.woodMetalBox.setItemText(4, _translate("MainWindow", "Отжим ригеля"))
        self.metalBox.setItemText(0, _translate("MainWindow", "Выбивание"))
        self.metalBox.setItemText(1, _translate("MainWindow", "Разрезание ножовкой"))
        self.metalBox.setItemText(2, _translate("MainWindow", "Газовая резка"))
        self.metalBox.setItemText(3, _translate("MainWindow", "Разрушение замка"))
        self.metalBox.setItemText(4, _translate("MainWindow", "Отжим двери"))
        self.metalBox.setItemText(5, _translate("MainWindow", "Отжим ригеля"))
        self.windowBox.setItemText(0, _translate("MainWindow", "Пролом стекла А1-А3"))
        self.windowBox.setItemText(1, _translate("MainWindow", "Пролом стекла Б1"))
        self.windowBox.setItemText(2, _translate("MainWindow", "Пролом стекла Б2"))
        self.windowBox.setItemText(3, _translate("MainWindow", "Пролом стекла Б3"))
        self.tacticsLabel_1.setText(_translate("MainWindow", "Тактика преодоления"))
        self.facilitiesLabel_1.setText(_translate("MainWindow", "Инженерные средства"))
        self.concrete.setText(_translate("MainWindow", "Бетонное ограждение"))
        self.gridWall.setText(_translate("MainWindow", "Сетчатое заграждение"))
        self.barbedWall.setText(_translate("MainWindow", "Колючая проволока"))
        self.concreteAKPBox.setItemText(0, _translate("MainWindow", "Перелаз"))
        self.concreteAKPBox.setItemText(1, _translate("MainWindow", "Подкоп"))
        self.concreteBox.setItemText(0, _translate("MainWindow", "Перелаз"))
        self.concreteBox.setItemText(1, _translate("MainWindow", "Подкоп"))
        self.gridWallBox.setItemText(0, _translate("MainWindow", "Перелаз"))
        self.gridWallBox.setItemText(1, _translate("MainWindow", "Пролом"))
        self.gridWallBox.setItemText(2, _translate("MainWindow", "Подкоп"))
        self.barbedWallBox.setItemText(0, _translate("MainWindow", "Перелаз"))
        self.barbedWallBox.setItemText(1, _translate("MainWindow", "Пролом"))
        self.barbedWallBox.setItemText(2, _translate("MainWindow", "Подкоп"))
        self.facilitiesLabel_2.setText(_translate("MainWindow", "Инженерные средства"))
        self.tacticsLabel_2.setText(_translate("MainWindow", "Тактика преодоления"))
        self.antiram.setText(_translate("MainWindow", "Противотаранное уст-во"))
        self.irFacility.setText(_translate("MainWindow", "Инфракрасный датчик"))
        self.gerkonFacility.setText(_translate("MainWindow", "Герконовый датчик"))
        self.elmechFacility.setText(_translate("MainWindow", "Электромеханический замок"))
        self.turnstileFacility.setText(_translate("MainWindow", "Турникет"))
        self.tacticsLabel_3.setText(_translate("MainWindow", "Технические средства обнаружения"))
        self.videoFacility.setText(_translate("MainWindow", "Видеокамера"))
        self.cardFacility.setText(_translate("MainWindow", "Считыватели карт"))
        self.alarmFacility.setText(_translate("MainWindow", "Кнопка тревоги"))
        self.glassFacility.setText(_translate("MainWindow", "Датчик разбития стекла"))
        self.warmFacility.setText(_translate("MainWindow", "Тепловой извещатель"))
        self.bioFacility.setText(_translate("MainWindow", "Биометрический считыватель"))
        self.capacityFacility.setText(_translate("MainWindow", "Емкостное средство"))
        self.radioFacility.setText(_translate("MainWindow", "Радиолучевое средство"))
        self.bombFacility.setText(_translate("MainWindow", "Обнаружитель ВВ"))
        self.piezoFacility.setText(_translate("MainWindow", "Пьезоэлектрическое"))
        self.tacticsBox.setTitle(_translate("MainWindow", "Тактика действия ТГ"))
        self.consistentTactic.setText(_translate("MainWindow", "Последовательная, с изменением маршрута"))
        self.intermediateTactic.setText(_translate("MainWindow", "С выходом на промежуточный рубеж\n"
"и без выхода на периметр "))
        self.groupBox.setTitle(_translate("MainWindow", "Ключевые точки"))
        self.intruder.setText(_translate("MainWindow", "Положение нарушителя"))
        self.PFZ.setText(_translate("MainWindow", "Положение ПФЗ"))
        self.startTG.setText(_translate("MainWindow", "Начальное положение ТГ"))
        self.endTG.setText(_translate("MainWindow", "Конечное положение ТГ"))
        self.wall.setText(_translate("MainWindow", "Стена"))
        self.passage.setText(_translate("MainWindow", "Проход"))
        self.clearButton.setText(_translate("MainWindow", "Очистить пути"))
