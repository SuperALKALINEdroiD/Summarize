import sys
from PyQt5.QtWidgets import *


# qsizepolicy to change size of button on window size change 

title_text = ''

def save_button_function(self):
    win = MainWindow()
    print(win.get_title())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()


        textbox = QPlainTextEdit(self)
        textbox.move(20, 20)
        textbox.setLayout(layout)
        textbox.setGeometry(100, 100, 200, 200)



        # title
        self.setWindowTitle("Summarizer")
        save_button = QPushButton("Save", self)
        save_button.clicked.connect(save_button_function)
        save_button.setGeometry(10, 10, 30, 30)


        # file_name
        file_name = QLineEdit(self)
        file_name.setGeometry(20, 20, 40, 80)


        def get_title():
            return file_name.text()

        self.showMaximized()







app = QApplication([])
main_window = MainWindow()
print('Starting....')
# Run the app
main_window.show()
app.exec_()
