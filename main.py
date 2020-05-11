import sys
import os
from travel_assistant import *
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
import json
from random import randint


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Data control
        self.countries = dict()
        self.users = dict()
        self.graphOfCountries = dict()

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
        # self.ui.actionLoad_Countries.triggered.connect(self.drawGraph)
        self.loadData()
        self.drawGraph()
        self.initStars()

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
                command = "self.ui.star{}_{}.setVisible(False)".format(i,j)
                exec(command)

    # Stars control
    def manageStars(self):
        if self.sender().objectName() == "places_sb":
            for i in range(2, 6):
                command = "self.ui.star1_{}.setVisible(False)".format(i)
                exec(command)

            for i in range(2, int(self.ui.places_sb.text()) + 1):
                command = "self.ui.star1_{}.setVisible(True)".format(i)
                exec(command)

        elif self.sender().objectName() == "food_sb":
            for i in range(2, 6):
                command = "self.ui.star2_{}.setVisible(False)".format(i)
                exec(command)

            for i in range(2, int(self.ui.food_sb.text()) + 1):
                command = "self.ui.star2_{}.setVisible(True)".format(i)
                exec(command)

        elif self.sender().objectName() == "clothes_sb":

            for i in range(2, 6):
                command = "self.ui.star3_{}.setVisible(False)".format(i)
                exec(command)

            for i in range(2, int(self.ui.clothes_sb.text()) + 1):
                command = "self.ui.star3_{}.setVisible(True)".format(i)
                exec(command)

    def loadData(self):
        if os.path.exists("users.json") and os.stat("users.json").st_size != 0:
            with open("users.json", 'r') as users_file:
                self.users = json.load(users_file)

        if os.path.exists("countries.json") and os.stat("countries.json").st_size != 0:
            with open("countries.json", 'r') as countries_file:
                self.countries = json.load(countries_file)

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
    #addNewCountry

    def saveCountries(self):
        with open("countries.json", 'w') as file:
            json.dump(self.countries, file, indent=5)


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
        self.saveUsers()

    def saveUsers(self):
        # Write the users in the file
        with open("users.json", 'w') as file:
            json.dump(self.users, file, indent=5)

    @Slot()
    def drawGraph(self):
        self.countries.clear()
        self.loadData()
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
