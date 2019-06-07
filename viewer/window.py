


from PyQt5 import QtWidgets, QtGui


folder = '/media/dstl-kaggle/sixteen_band/'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, image):
        super().__init__()

        self.image = image

        self.initUI()

        self.scene.set_image(image.get_filename())


    def initUI(self):

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.resize(800, 600)

        self.view = QtWidgets.QGraphicsView(self.centralwidget)
        self.verticalLayout.addWidget(self.view)

        self.scene = PictureScene()
        self.view.setScene(self.scene)



class PictureScene(QtWidgets.QGraphicsScene):

    def __init__(self):
        super().__init__()

        self.background = QtWidgets.QGraphicsPixmapItem()
        self.addItem(self.background)

    def set_image(self, img):
        self.background.setPixmap(QtGui.QPixmap(img))

    
