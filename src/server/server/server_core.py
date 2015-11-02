import time
import sys

from src.server.server.server_configuration_manager import server_configuration_manager
from src.commons.utils.logger import logger

class server_core(object):
	def __init__(self, json_configuration_file):
		self.config = self.init_config(json_configuration_file)
		self.server_is_running = True
		self.agents_threads_are_started = False


	def init_config(self, json_configuration_file):
		return server_configuration_manager(json_configuration_file)

	def run(self):
		logger.info("Hestia is running !")

		while self.server_is_running:
			if not self.agents_threads_are_started:
				self.start_all_agents_thread()

			try:
				if self.config.all_ressources_are_available():
					self.delay()
				else:
					self.configuration_error_handler()
			except KeyboardInterrupt:
				self.server_is_running = False
			except:
				logger.error("[CRITICAL ERROR] ")
				self.server_is_running = False

		logger.info("Hestia is quitting !")

		sys.exit(0)

	def delay(self):
		time.sleep(5)

	def configuration_error_handler(self):
		self.config.start_reconection()
		self.stop_all_agents_thread()
		logger.error("Connection failed !")

		while (self.config.have_to_be_waited()):
			logger.info("Connection lost Hestia is trying to reconnect")
			self.delay()

		if not self.config.can_run():
			self.server_is_running = False

	def stop_all_agents_thread(self):
		logger.info("Stoping Hestia's agents")

		for agent in self.config.get_agents():
			agent.stop_command_thread()

		logger.info("Hestia's agents stopped")

		self.agents_threads_are_started = False

	def start_all_agents_thread(self):
		logger.info("Launching Hestia's agents")

		for agent in self.config.get_agents():
			agent.start_command_thread()

		logger.info("Hestia's agents launched")

		self.agents_threads_are_started = True
