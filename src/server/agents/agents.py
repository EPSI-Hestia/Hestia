from src.commons.utils.pin import pin
from src.commons.dao.model.agent_model import agent_model
from src.commons.utils.logger import logger

from threading import Thread
import time

class agents(object):

	def __init__(self,  agent_data):
		self.name =  agent_data['name']
		self.pin = pin( agent_data['pin'],  agent_data['pin_mode'],  agent_data['pin_type'])
		self.stop = False
		self.model = agent_model(agent_data["mongo_datas"], agent_data['board_name'], self.name)


	def start_command_thread(self):
			self.command_thread = Thread(target=self.update)
			self.command_thread.daemon = True
			self.command_thread.start()


	def stop_command_thread(self):
		self.stop = True

	def update(self):
		while not self.stop:
			self.refresh()
			time.sleep(0.5)

	def value(self):
		return ""

	def refresh(self):
		last_entries = self.model.get_last_entries(5)

		event_find = False
		value_to_write = ""

		for entry in last_entries:
			if entry["mode"] == "r":
				event_find = True
				value_to_write = entry["value"]
				self.model.disengage_event(entry["datetime"])

		if event_find:
			value = value_to_write
			self.pin.write(value)
			logger.event(self.name + " value has been updated : " + str(self.value()))

		self.model.insert(self.value())
		logger.monitoring(self.name + " value read : " + str(self.value()))

	def __del__(self):
		self.stop_command_thread()