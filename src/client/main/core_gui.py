from PyQt4.QtGui import *
from PyQt4.QtCore import *

from src.client.main.all_agents_widgets import all_agent_widget
from src.client.main.home_widget import home_widget

import src.res.images_rc

class core_gui(QWidget):
    def __init__(self):
        super(core_gui, self).__init__()
        self.number_of_tab = -1
        self.initUI()


    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.help_label = QLabel()
        pix = QPixmap(":/Help")
        self.help_label.setFixedWidth(50)
        self.help_label.setFixedHeight(50)
        pix = pix.scaled(self.help_label.size(), Qt.KeepAspectRatio)
        self.help_label.setPixmap(pix)
        self.help_label.setToolTip(QString("Use the two bottom button to add or remove Tabs \n\rYou can supervise one board on each Tab"))

        self.main_layout.addWidget(self.help_label)

        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/Add"), QIcon.Normal, QIcon.Off)
        self.buttonAddTab = QPushButton('Add Tab')
        self.buttonAddTab.setIcon(icon)
        self.buttonAddTab.setIconSize(QSize(24,24))
        self.buttonAddTab.setFixedWidth(200)
        self.connect(self.buttonAddTab, SIGNAL("clicked()"), self, SLOT("add_tab()"))
        self.main_layout.addWidget(self.buttonAddTab)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/Remove"), QIcon.Normal, QIcon.Off)
        self.buttonRemoveTab = QPushButton('Remove Tab')
        self.buttonRemoveTab.setIcon(icon)
        self.buttonRemoveTab.setIconSize(QSize(24,24))
        self.buttonRemoveTab.setFixedWidth(200)
        self.connect(self.buttonRemoveTab, SIGNAL("clicked()"), self, SLOT("remove_tab()"))
        self.main_layout.addWidget(self.buttonRemoveTab)

        self.setLayout(self.main_layout)
        self.setWindowTitle('Circe')

        self.add_home_tab()

    def add_home_tab(self):
        self.number_of_tab += 1
        w = home_widget()
        self.tabs.addTab(w, "Home")

    @pyqtSlot()
    def add_tab(self):
        text, result = QInputDialog.getText(self, "New Tab",
                                            "Please enter new Tab Name")
        if result:
            self.number_of_tab += 1
            self.agents_widget = all_agent_widget()
            self.tabs.addTab(self.agents_widget, text + " - " + str(self.number_of_tab))
            #self.tabs.currentIndex(self.number_of_tab)

    @pyqtSlot()
    def remove_tab(self):
        if self.number_of_tab >= 0:
            self.tabs.removeTab(self.number_of_tab)
            self.number_of_tab -= 1