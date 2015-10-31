import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from src.main.agents.agent_widget import agent_widget
from src.main.configuration_loader import *

class circe_main(QWidget):
    def __init__(self):
        super(circe_main, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        self.setGeometry(30,30, 30, 30)
        self.setWindowTitle('Circe')

        self.add_basic_widgets()
        self.show()

    @pyqtSlot()
    def select_configuration_file(self):
        self.load_configuration_file()

        if(self.configuration_loader.is_loaded):
            self.remove_all_widgets()
            self.add_basic_widgets()
            self.create_agents()

    def remove_all_widgets(self):
        for i in range(self.layout().count()): self.layout().itemAt(i).widget().close()

    def create_agents(self):
        self.number_of_widgets_per_row = 4
        self.x_limit = 10
        self.y_limit = 3

        self.number_of_widgets_max = len(self.configuration_loader.agents_datas)
        self.number_of_widgets_created = 0

        for x in range(1, self.x_limit):
            for y in range(0, self.y_limit):
                if(self.number_of_widgets_created < self.number_of_widgets_max):
                    datas = {}
                    datas["mongo"] = self.configuration_loader.mongo_datas
                    datas["board"] = self.configuration_loader.board
                    datas["agent"] = self.configuration_loader.agents_datas[self.number_of_widgets_created]

                    new_agent = agent_widget(datas)
                    self.layout().addWidget(new_agent, x, y)
                    self.number_of_widgets_created += 1

    def add_basic_widgets(self):
        title = QLabel('Circe the minimalist generic client for Hestia')
        buttonLoadConfig = QPushButton('Load configuration')
        self.connect(buttonLoadConfig, SIGNAL("clicked()"), self, SLOT("select_configuration_file()"))
        self.layout().addWidget(title, 0, 0)
        self.layout().addWidget(buttonLoadConfig, 0, 1)

    def load_configuration_file(self):
        try:
            self.configuration_loader = server_config(QFileDialog.getOpenFileName())
        except ConfigurationException, e:
            print e
            QApplication.quit()

def main():
    app = QApplication(sys.argv)
    ex = circe_main()
    sys.exit(app.exec_())

