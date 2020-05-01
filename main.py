import sys
from travel_assistant import *
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
import json


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.countries = []
        self.users = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.views.setCurrentIndex(0)
        self.ui.travel_button.clicked.connect(self.changePage)

        self.ui.pushButton.clicked.connect(self.drawGraph)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)



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
        self.loadUsers()  # Se cargará el json de los usuarios
        self.loadCountries()  # Se cargara el json de paises
        pen = QPen()
        pen.setWidth(3)
        color = QColor(12,43,22)
        pen.setColor(color)
    #drawGraph

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
