

from PyQt5 import QtCore



class Controller(QtCore.QObject):

    def __init__(self, app, window, image):

        super().__init__(app)

        self.app = app
        self.window = window
        self.image = image


