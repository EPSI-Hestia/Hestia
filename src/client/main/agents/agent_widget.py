from PyQt4.QtGui import *
from PyQt4.QtCore import *

from src.client.main.circe_listener import circe_listener
from src.client.main.details_widget import details_widget

import src.res.images_rc

class agent_widget(QWidget):
    def __init__(self, datas):
        super(agent_widget, self).__init__()
        self.listener = circe_listener(datas)
        self.init_UI(datas["agent"])
        self.listener.start_listening()
        self.setStyleSheet("""
           /* other rules go here */

           QWidget[bordered="true"] {
                background-color: white;
                border:1px solid black;
                border-radius:5px;
            };

           QWidget[bordered="false"] {background-color: palette(base)};
            """)


    def init_UI(self, datas):
        self.setProperty("bordered", True)
        self.setFixedSize(300, 250)

        self.grid = QGridLayout()

        self.grid.setSpacing(10)

        self.label_name = QLabel(datas["name"])
        self.label_name.setObjectName('label_name')
        self.label_name.setStyleSheet('QLabel#label_name {color: #000ddd; font-size:15px;}')

        self.grid.addWidget(self.label_name, 0, 0)
        self.label_lib_actual_value = QLabel("Actual value :")

        icon = QIcon()
        icon.addPixmap(QPixmap(":/Search"), QIcon.Normal, QIcon.Off)

        self.buttonDetails = QPushButton('Details')
        self.buttonDetails.setIcon(icon)
        self.buttonDetails.setIconSize(QSize(24,24))
        self.buttonDetails.setFixedWidth(100)
        self.connect(self.buttonDetails, SIGNAL("clicked()"), self, SLOT("show_details()"))
        self.grid.addWidget(self.buttonDetails, 0, 1)

        if datas["pin_type"] == "digital":
            self.value_digital_widgets()
        elif datas["pin_type"] == "analogic":
            self.value_analogic_widgets()

        self.listener.value_updated.connect(self.refresh_value)

        if datas["pin_mode"] == "OUTPUT":
            if datas["pin_type"] == "digital":
                self.value_update_digital_widgets()
                self.button_write.clicked.connect(self.digital_value_to_write)
            elif datas["pin_type"] == "analogic":
                self.value_update_analogic_widgets()
                self.button_write.clicked.connect(self.analogic_value_to_write)

        self.label_last_date_lib = QLabel("last update : ")
        self.label_last_date_value = QLabel("Never updated")
        self.grid.addWidget(self.label_last_date_lib, 3, 0)
        self.grid.addWidget(self.label_last_date_value, 3, 1)

        self.style().unpolish(self)
        self.style().polish(self)

        self.setLayout(self.grid)

    @pyqtSlot()
    def refresh_value(self):
        value = self.listener.get_value()
        last_date = self.listener.get_date()

        try:
            float(value)
        except ValueError:
            value = 0

        if  str(value) == "1.0":
            value = "ON"
        elif str(value) == "0.0":
            value = "OFF"

        last_date = str(last_date)

        self.label_actual_value.setText(QString(value))
        self.label_last_date_value.setText(QString(last_date))

    @pyqtSlot()
    def digital_value_to_write(self):
        value = 0

        if(self.input_new_value.currentText() == "ON"):
            value = 1

        self.listener.model.insert(value)

    @pyqtSlot()
    def analogic_value_to_write(self):
        self.listener.model.insert(str(self.input_new_value.value()))

    @pyqtSlot()
    def show_details(self):
        w = details_widget(self, self.listener.get_last_entries(50))
        w.show()

    def value_update_digital_widgets(self):
        self.label_lib_change_value = QLabel("Change value :")
        self.input_new_value = QComboBox()
        self.input_new_value.addItem("ON")
        self.input_new_value.addItem("OFF")

        self.button_write = QPushButton("Write")

        self.grid.addWidget(self.label_lib_change_value, 2, 0)
        self.grid.addWidget(self.input_new_value, 2, 1)
        self.grid.addWidget(self.button_write, 2, 2)

    def value_digital_widgets(self):
        self.label_actual_value = QLabel("off")
        self.grid.addWidget(self.label_lib_actual_value, 1, 0)
        self.grid.addWidget(self.label_actual_value, 1, 1)

    def value_analogic_widgets(self):
        self.label_actual_value = QLabel("342")
        self.grid.addWidget(self.label_lib_actual_value, 1, 0)
        self.grid.addWidget(self.label_actual_value, 1, 1)

    def value_update_analogic_widgets(self):
        self.label_lib_change_value = QLabel("Change value :")

        self.input_new_value = QSpinBox()

        self.input_new_value.setMaximum(1024)
        self.input_new_value.setMinimum(0)

        self.button_write = QPushButton("Write")
        self.grid.addWidget(self.label_lib_change_value, 2, 0)
        self.grid.addWidget(self.input_new_value, 2, 1)
        self.grid.addWidget(self.button_write, 2, 2)

