import sys
from travel_assistant import *
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from country import Country


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
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

    @Slot()
    def drawGraph(self):
        test = Country("Webos", "2", "3", "5", 200, (2, 5))
        pen = QPen()
        pen.setWidth(3)
        color = QColor(12,43,22)
        pen.setColor(color)
        coordinates = test.getCoordinates()
        self.scene.addEllipse(coordinates[0], coordinates[0], 10, 10, pen)

    #drawGraph

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
