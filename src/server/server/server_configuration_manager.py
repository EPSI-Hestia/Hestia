from threading import Thread
import time

from src.commons.utils.configuration_loader import configuration_loader
from src.server.agents.agent_factory import agent_factory
from src.commons.dao.model.board_model import board_model
from src.commons.utils.com_connexion import com_connexion
from src.commons.utils.logger import logger

class server_configuration_manager(object):
	def __init__(self, json_configuration_file):
		self.init_attr(json_configuration_file)
		self.server_can_run = False
		self.is_trying_to_reconected = False

	def start_reconection(self):
			self.is_trying_to_reconected = True
			self.command_thread = Thread(target=self.try_to_reconnect)
			self.command_thread.daemon = True
			self.command_thread.start()


	def init_attr(self, json_configuration_file):
		self.configuration =  configuration_loader(json_configuration_file)

		if self.configuration.is_loaded:
			logger.info("Initialize communication with Hestia city")
			self.board_model = board_model(self.configuration.mongo_datas)
			self.set_up_databases()
			logger.info("Communication with Hestia city established")

			logger.info("Initialisation of the Hestia agent's")
			self.agents = []
			self.initialize_agents()
			logger.info("Hestia agent's ready")
			self.server_can_run = True

	def initialize_agents(self):
		for agent_data in  self.configuration.agents:
			agent_data['board_name'] =  self.configuration.board['name']
			agent_data['mongo_datas'] = self.configuration.mongo_datas
			self.agents.append(agent_factory.create(agent_data))

	def set_up_databases(self):
		self.board_model.flush_collection(self.configuration.board['name'])

	def all_ressources_are_available(self):
		self.server_can_run = self.configuration.is_loaded and com_connexion.is_available() and self.board_model.connection_established
		return self.server_can_run

	def try_to_reconnect(self):
		number_of_reconnection_attempt = 6
		delay = 10

		for i in range(0, number_of_reconnection_attempt):
			if self.server_can_run:
				self.is_trying_to_reconected = False
				pass

			try:
				self.server_can_run = self.all_ressources_are_available()
			except:
				self.is_trying_to_reconected = True

			if not self.server_can_run:
				logger.error("Reconnection failed !")
				time.sleep(delay)
			else:
				logger.info("Hestia is coming back !")

	def can_run(self):
		return self.server_can_run

	def get_agents(self):
		return self.agents

	def have_to_be_waited(self):
		return self.is_trying_to_reconected