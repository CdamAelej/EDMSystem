import logowanie_box_main
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])

    widget = logowanie_box_main.OknoLogowania()
    widget.show()

    #app.exec_()






