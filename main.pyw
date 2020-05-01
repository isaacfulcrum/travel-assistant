import sys
from travel_assistant import *


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.views.setCurrentIndex(0)
        self.ui.travel_button.clicked.connect(self.changePage)

    def changePage(self):
        self.ui.views.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
