from PyQt4.QtGui import *
from PyQt4.QtCore import *

class details_widget(QWidget):
    def __init__(self, datas, parent=None):
        super(details_widget, self).__init__(parent)
        self.initUi(datas)

    def initUi(self, datas):
        self.grid_layout = QGridLayout()

        i = 0

        for d in datas:
            lab = QLabel(d["value"])
            self.grid_layout.addWidget(lab, 0, i)
            i += 1

        self.setLayout(self.grid_layout)
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Details widget')
        self.show()
