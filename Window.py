from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        self.lineEdit = ""
        self.plainTextEdit = ""


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(170, 10, 80, 23))
        self.save_button.setObjectName("save_button")
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.save_file)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 113, 23))
        self.filename = self.lineEdit.text()

        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 761, 531))
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setWindowTitle("Summarizer")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save_button.setText(_translate("MainWindow", "Save"))


    def save_file(self):
        filename = self.lineEdit.text()
        corpus = self.plainTextEdit.toPlainText()
        file = open(f'/home/AlkalineD/Documents/Project_file/{filename}', 'w')
        file.write(corpus)
        file.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
