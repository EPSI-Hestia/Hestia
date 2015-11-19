from PyQt4.QtGui import *
from PyQt4.QtCore import *

from src.client.main.all_agents_widgets import all_agent_widget
import src.res.images_rc

class core_gui(QWidget):
    def __init__(self):
        super(core_gui, self).__init__()
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget()

        pixmap = QPixmap(":/Add")
        self.label = QLabel()
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)
        self.setWindowTitle('Circe')


        self.agents_widget = all_agent_widget()
        self.tabs.addTab(self.agents_widget, "Arduino1")

        self.agents_widget2 = all_agent_widget()
        self.tabs.addTab(self.agents_widget2, "Arduino2")


