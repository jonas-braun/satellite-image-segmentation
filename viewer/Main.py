#!/usr/bin/env python3



import sys


from PyQt5.QtWidgets import (QApplication)

from model import Image
from window import MainWindow
from controller import Controller





if __name__ == '__main__':


    image = Image()

    app = QApplication(sys.argv)


    mainWindow = MainWindow(image)
    mainWindow.show()

    controller = Controller(app, mainWindow, image)

    sys.exit(app.exec_())

