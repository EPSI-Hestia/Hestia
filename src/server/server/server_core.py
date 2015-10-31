import time
import sys

from src.commons.utils.configuration_loader import configuration_loader
from src.server.agents.agent_factory import agent_factory
from src.commons.dao.model.board_model import board_model
from src.commons.utils.com_connexion import com_connexion
from src.commons.utils.logger import logger

class server_core(object):
	def __init__(self, json_configuration_file):
		self.init_attr(json_configuration_file)

		if self.all_ressources_are_available():
			self.run()

	def init_attr(self, json_configuration_file):
		self.configuration = configuration_loader(json_configuration_file)
		self.server_is_running = False

		if self.configuration.is_loaded:
			logger.info("Initialize communication with Hestia city")
			self.board_model = board_model(self.configuration.mongo_datas)
			self.set_up_databases()
			logger.info("Communication with Hestia city established")

			logger.info("Initialisation of the Hestia agent's")
			self.server_is_running = True
			self.agents = []
			self.initialize_agents()
			logger.info("Hestia agent's ready")

	def initialize_agents(self):
		for agent_data in  self.configuration.agents:
			agent_data['board_name'] =  self.configuration.board['name']
			agent_data['mongo_datas'] = self.configuration.mongo_datas
			self.agents.append(agent_factory.create(agent_data))

	def stop_all_agents_thread(self):
		for agent in self.agents:
			agent.stop_command_thread()

	def start_all_agents_thread(self):
		for agent in self.agents:
			agent.start_command_thread()

	def set_up_databases(self):
		self.board_model.flush_collection(self.configuration.board['name'])

	def all_ressources_are_available(self):
		return self.configuration.is_loaded and com_connexion.is_available(True) and self.board_model.connection_established

	def run(self):
		logger.info("Hestia agent's are working ...")
		self.start_all_agents_thread()

		while self.server_is_running:
			try:
				self.server_is_running = com_connexion.is_available()

				if self.server_is_running:
					time.sleep(5)
			except KeyboardInterrupt:
				self.server_is_running = False
			except:
				logger.error("[CRITICAL ERROR] ")
				self.server_is_running = False

		self.stop_all_agents_thread()
		logger.info("Hestia agent's stop working !")

		sys.exit(0)