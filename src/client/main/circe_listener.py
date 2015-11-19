from src.commons.dao.model.agent_model import agent_model

from threading import Thread
from PyQt4.QtCore import *
import time


class circe_listener(QObject):
    value_updated = pyqtSignal()

    def __init__(self, datas):
        QObject.__init__(self)
        self.listener = self.create_listener()
        self.model = agent_model(datas["mongo_datas"], datas['board_name']["name"], datas["agent"]["name"])
        self.listening = False

    def _del__(self):
        self.listening = False


    def create_listener(self):
        self.listening_thread = Thread(target=self.listen)
        self.listening_thread.daemon = True


    def listen(self):
        while self.listening:
            self.value = str(self.model.get_last_entry_value_and_date()["value"])
            self.date = str(self.model.get_last_entry_value_and_date()["datetime"])
            self.value_updated.emit()
            time.sleep(0.5)

    def start_listening(self):
        self.listening = True
        self.listening_thread.start()

    def get_value(self):
        return self.value

    def get_date(self):
        return self.date

    def get_last_entries(self, number_of_entries_to_get):
        return self.model.get_last_entries(number_of_entries_to_get)