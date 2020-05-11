import sys
import os
from travel_assistant import *
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
import json
import pathlib
from random import randint


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Data control
        self.database = dict()
        self.countries = dict()
        self.users = dict()
        self.graphOfCountries = dict()
        self.path = str(pathlib.Path(__file__).parent.absolute()) + '/database.json'

        # Ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        # Views control
        self.ui.views.setCurrentIndex(0)
        self.ui.travel_button.clicked.connect(self.changePage)
        self.ui.ready_button.clicked.connect(self.changePage)

        # Manage stars
        self.ui.clothes_sb.valueChanged.connect(self.manageStars)
        self.ui.food_sb.valueChanged.connect(self.manageStars)
        self.ui.places_sb.valueChanged.connect(self.manageStars)

        self.ui.listWidget.addItem("WELCOME TO TRAVEL ASSISTANT")
        self.scene = QGraphicsScene()
        self.ui.gvWorldMap.setScene(self.scene)
        # self.ui.load_Data.triggered.connect(self.loadFile)
        self.loadData()
        self.drawGraph()
        self.initStars()

    def loadData(self):
        if os.path.exists(self.path) and os.stat(self.path).st_size != 0:
            with open(self.path, 'r') as data_file:
                self.database = json.load(data_file)
                self.users = self.database["Users"]
                self.countries = self.database["Countries"]

    def saveData(self):
        self.database["Users"] = self.users
        self.database["Countries"] = self.countries
        with open(self.path, 'w') as data_file:
            json.dump(self.database, data_file, indent=5)

    def changePage(self):
        if self.sender().objectName() == "travel_button":
            self.ui.views.setCurrentIndex(1)
        elif self.sender().objectName() == "ready_button":
            self.addNewUser()
            self.ui.views.setCurrentIndex(2)

    # Stars are placed in their initial position
    def initStars(self):
        for i in range(1, 4):
            for j in range(2, 6):
                command = "self.ui.star{}_{}.hide()".format(i,j)
                exec(command)

    # Stars control
    def manageStars(self):
        if self.sender().objectName() == "places_sb":
            for i in range(2, 6):
                command = "self.ui.star1_{}.hide()".format(i)
                exec(command)

            for i in range(2, int(self.ui.places_sb.text()) + 1):
                command = "self.ui.star1_{}.show()".format(i)
                exec(command)

        elif self.sender().objectName() == "food_sb":
            for i in range(2, 6):
                command = "self.ui.star2_{}.hide()".format(i)
                exec(command)

            for i in range(2, int(self.ui.food_sb.text()) + 1):
                command = "self.ui.star2_{}.show()".format(i)
                exec(command)

        elif self.sender().objectName() == "clothes_sb":

            for i in range(2, 6):
                command = "self.ui.star3_{}.hide()".format(i)
                exec(command)

            for i in range(2, int(self.ui.clothes_sb.text()) + 1):
                command = "self.ui.star3_{}.show()".format(i)
                exec(command)

    # addNewCountry
    def addNewCountry(self):
        #Metodo de prueba para ver los datos que lleva cada diccionario de cada pais
        #Hay que cambiarlo para que tenga un evento al momento de querer cargar uno nuevo
        country = {
            "name": "Mexico",
            "starsClothes": 3,
            "starsFood": 5,
            "starsTourism": 4,
            "cost": 465,
            "coordinates": (50,35)
        }
        return country

    # Add a new user
    def addNewUser(self):
        
        name = self.ui.nameText.text()
        budget = int(self.ui.budgetText.text())
        places = int(self.ui.places_sb.text())
        food = int(self.ui.food_sb.text())
        clothes = int(self.ui.clothes_sb.text())

        self.users[name] = dict()
        self.users[name]["budget"] = budget
        self.users[name]["food"] = food
        self.users[name]["places"] = places
        self.users[name]["clothes"] = clothes
        self.saveData()

    @Slot()
    def drawGraph(self):
        # self.countries.clear()
        # self.loadData()
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(0,0,0))
        self.scene.addEllipse(0, 0, 1, 1, pen)
        self.scene.addEllipse(948, 445, 1, 1, pen)
        #Esto es para tener una zona de trabajo de 950x447
        print(self.scene.height())
        print(self.scene.width())

        for node in self.countries:
            origin = (node["coordinates"][0],node["coordinates"][1])
            if origin not in self.graphOfCountries:
                self.graphOfCountries[origin] = []
            for adjacencies in node["adjacencies"]:
                self.graphOfCountries[origin].append(adjacencies)

        for country, adjacencies in self.graphOfCountries.items():
            pen.setWidth(5)
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            color = QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(country[0],country[1],5,5,pen)
            pen.setWidth(3)
            for element in adjacencies:
                otherCountry = element[0]
                self.scene.addLine(country[0]+1,country[1]+1, otherCountry[0]+1,otherCountry[1]+1, pen)

    #drawGraph
    def wheelEvent(self, event):
        if(event.delta() > 0):
            self.ui.gvWorldMap.scale(1.2,1.2)
        else:
            self.ui.gvWorldMap.scale(0.8,0.8)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
