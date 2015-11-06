from PyQt4.QtGui import *
from PyQt4.QtCore import *

from src.client.main.agents.agent_widget import agent_widget
from src.commons.utils.configuration_loader import *

class core_gui(QWidget):
    def __init__(self):
        super(core_gui, self).__init__()

        self.number_of_widgets_per_row = 3
        self.selected_agents = []

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.setGeometry(30, 30, 30, 30)
        self.setWindowTitle('Circe')

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.add_basic_widgets()

    def add_basic_widgets(self):
        title = QLabel('Circe the minimalist generic client for Hestia')

        buttonLoadConfig = QPushButton('Load configuration')
        self.connect(buttonLoadConfig, SIGNAL("clicked()"), self, SLOT("select_configuration_file()"))

        self.layout().addWidget(title)
        self.layout().addWidget(buttonLoadConfig)

    def load_configuration_file(self):
        try:
            self.configuration_loader = configuration_loader(QFileDialog.getOpenFileName())
        except ConfigurationException, e:
            print e
            QApplication.quit()

    @pyqtSlot()
    def select_configuration_file(self):
        self.load_configuration_file()

        if(self.configuration_loader.is_loaded):
            for i in range(self.layout().count()): self.layout().itemAt(i).widget().close()
            self.add_agents_selector_widget()
            self.main_layout.addLayout(self.grid)

    def add_agents_selector_widget(self):
        self.list = QListView()
        model_list = QStandardItemModel(self.list)

        agents_name = []
        for agent in self.configuration_loader.agents_datas: agents_name.append(agent["name"])

        self.list.setMinimumHeight((len(agents_name) * 10))

        for name in agents_name:
            item = QStandardItem(name)
            item.setData(name)
            item.setCheckable(True)
            model_list.appendRow(item)

        self.list.clicked.connect(self.agent_selected)
        self.list.setModel(model_list)

        self.layout().addWidget(self.list)

    @pyqtSlot()
    def agent_selected(self):
        model = self.list.model()

        self.selected_agents = []

        for index in range(model.rowCount()):
            item = model.item(index)
            if item.checkState():
                self.selected_agents.append(item.data().toString())
                
        self.create_agents()

    def remove_all_agents_widgets(self):
        for i in range(self.grid.layout().count()):
            self.grid.layout().itemAt(i).widget().close()

    def create_agents(self):
        self.remove_all_agents_widgets()

        number_of_widgets_max = len(self.selected_agents)
        number_of_widgets_created = 0
        number_of_widget_in_actual_row = 0
        number_of_row_created = 0

        cpt = -1

        while number_of_widgets_created < number_of_widgets_max:
            for i in range(0, len(self.configuration_loader.agents_datas)):
                if self.configuration_loader.agents_datas[i]["name"] == self.selected_agents[number_of_widgets_created]:
                    cpt = i

            if cpt is not -1:
                datas = {}
                datas["mongo_datas"] = self.configuration_loader.mongo_datas
                datas["board_name"] = self.configuration_loader.board
                datas["agent"] = self.configuration_loader.agents_datas[cpt]

                if number_of_widget_in_actual_row >= self.number_of_widgets_per_row:
                    number_of_widget_in_actual_row = 0
                    number_of_row_created += 1

                new_agent = agent_widget(datas)
                self.grid.layout().addWidget(new_agent, number_of_row_created, number_of_widget_in_actual_row)

                number_of_widgets_created += 1
                number_of_widget_in_actual_row += 1