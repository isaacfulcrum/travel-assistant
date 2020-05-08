import sys
from travel_assistant import *
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
import json
from random import randint


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.countries = []
        self.graphOfCountries = dict()
        self.users = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.views.setCurrentIndex(0)
        self.ui.travel_button.clicked.connect(self.changePage)
        self.ui.pushButton.clicked.connect(self.drawGraph)

        self.ui.listWidget.addItem("WELCOME TO TRAVEL ASSISTANT")

        self.scene = QGraphicsScene()
        self.ui.gvWorldMap.setScene(self.scene)

        self.ui.actionLoad_Countries.triggered.connect(self.drawGraph)


    def changePage(self):
        self.ui.views.setCurrentIndex(1)

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
        fileLocation = QFileDialog.getSaveFileName(self, "SaveCountries", ".", "JSON")

        with open(fileLocation[0], 'w') as file:
            json.dump(self.countries, file, indent=5)
    #saveCountries

    def laodCountries(self):
        fileLocation = QFileDialog.getOpenFileName(self, "LoadCountries", ".", "JSON(*.json)")

        with open(fileLocation[0], 'r') as file:
            self.countries = json.load(file)
    #loadCountries

    def addNewUser(self):
        #Metodo de prueba para ver los datos que lleva cada diccionario de cada usuario
        #Hay que cambiarlo para que tenga un evento al momento de querer cargar uno nuevo
        country = {
            "name": "Juan",
            "capital": 1500,
            "countryOrigin": "Mexico",
            "countryDestiny": "Argentina",
            "tasteForFood": 5,
            "tasteForClothes": 3,
            "tasteForTourism": 6
        }

        return country
    #addNewCountry

    def saveUsers(self):
        fileLocation = QFileDialog.getSaveFileName(self, "SaveUsers", ".", "JSON")

        with open(fileLocation[0], 'w') as file:
            json.dump(self.users, file, indent=5)
    #saveCountries

    def loadUsers(self):
        fileLocation = QFileDialog.getOpenFileName(self, "LoadUsers", ".", "JSON(*.json)")

        with open(fileLocation[0], 'r') as file:
            self.users = json.load(file)
    #loadCountries

    @Slot()
    def drawGraph(self):
        self.countries.clear()
        self.laodCountries()
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
