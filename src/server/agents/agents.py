from utils.pin import pin
from dao.model.agent_model import agent_model
from utils.logger import logger

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
		last_entry = self.model.get_last_entry()

		if last_entry["mode"] == "r":
			value = last_entry["value"]
			self.pin.write(value)
			logger.event(self.name + " value has been updated : " + str(self.value()))

		self.model.insert(self.value())
		logger.monitoring(self.name + " value read : " + str(self.value()))

	def __del__(self):
		self.stop_command_thread()