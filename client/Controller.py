from view.view import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import requests


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):

    def translate(self):
        """
        Methode holt sich die Daten aus dem Client Interface und schickt diese an die API
        """
        payload = {"text": self.ui.inputField.toPlainText()}
        self.resp = requests.get("http://localhost:8080/detect", params=payload).json()
        self.set_output()

    def set_output(self):
        """
        Methode setzt das Output Feld und gibt die Empfangenen Werte
        """
        self.ui.outputField.clear()
        print(self.resp)
        output = "reliable: <b>" + str(self.resp["reliable"]) + \
                 "</b><br> language: <b>" + str(self.resp["language"] +
                                                "</b><br> probability: <b>" + str(self.resp["prob"]) + "</b>")
        self.ui.outputField.append(output)

    def __init__(self, parent=None):
        """
        Init Methode der Controller Klasse
        :param parent:
        """
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.url = "http://0.0.0.0:8080/detect"
        self.text = ""
        self.resp= ""
        self.ui.checkButton.clicked.connect(self.translate)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())
