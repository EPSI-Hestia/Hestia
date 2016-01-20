from PyQt4.QtGui import *
from PyQt4.QtCore import *

import src.res.images_rc

class home_widget(QWidget):
    def __init__(self):
        super(home_widget, self).__init__()
        self.initUi()

    def initUi(self):
        self.main_layout = QGridLayout()

        self.title_label = QLabel("Welcome to Hestia")
        self.title_label.setStyleSheet('font-size: 18pt;')
        self.main_layout.addWidget(self.title_label, 0, 0)

        self.main_image = QLabel()
        pix = QPixmap(":/Map")
        pix = pix.scaled(self.main_image.size(), Qt.KeepAspectRatio)
        self.main_image.setPixmap(pix)
        self.main_layout.addWidget(self.main_image, 1, 0)

        self.content_label = QLabel("Hestia is a remote distributed solution designed to take advantage from Arduino based microcontrollers\n\r\n\rHestia is composed of severals layers :\n\r\n\r- Hestia nodes are server directly plug to nanpy arduino board, multiple Hestia nodes can be connected to the same Hestia City\n\r\n\r- Hestia City is a MongoDB database centralizing all the data extract from the Hestia nodes\n\r\n\r- A WebService enable outside webclient to acces to Hestia datas without autentification\n\r\n\r- To finish Circe client can be use to monitor Hestia activities directly over Hestia city\n\r\n\rHestia can be use to monitor and to control multiple arduino board easily over the cloud !")
        self.main_layout.addWidget(self.content_label, 1, 1)

        self.setLayout(self.main_layout)