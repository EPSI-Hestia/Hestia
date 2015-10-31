from src.commons.utils.json_parser import json_parser

class ConfigurationException(Exception):
    pass

class configuration_loader(object):

	def __init__(self, json_configuration_file):
		self.init_attr(json_configuration_file)
		self.parse_configuration_file()

	def init_attr(self, json_configuration_file):
		self.parser = json_parser(json_configuration_file)
		self.mongo_properties = {}
		self.board_properties = {}
		self.agents_datas = []
		self.composite_datas = []
		self.json_file_loaded = True

	def parse_configuration_file(self):
		if self.parser.check_if_file_exists_and_its_valid_json():
			try:
				self.set_mongo_properties()
				self.set_board_properties()
				self.set_agents_datas()
				self.set_composites_datas()
			except ConfigurationException as e:
				print e
				self.json_file_loaded = False
		else:
			self.json_file_loaded = False

	def set_mongo_properties(self):
		self.mongo_properties = self.parser.get_value_by_key("mongo")

		if self.mongo_properties is "":
			raise ConfigurationException("Hestia Node network configuration isn't present")

		if not "mongo_host" in self.mongo_properties.keys() or not "mongo_port" in self.mongo_properties.keys() :
			raise ConfigurationException("Hestia Node missing some keys")

		if self.mongo_properties["mongo_host"] is "" or self.mongo_properties["mongo_port"] is "" or (not int(self.mongo_properties["mongo_port"]) ):
			raise ConfigurationException("Board's name not valid")

	def set_board_properties(self):
		self.board_properties = self.parser.get_value_by_key("board")

		if self.board_properties is "":
			raise ConfigurationException("Board's node isn't present")

		if not "name" in self.board_properties.keys():
			raise ConfigurationException("Board's missing some keys")

		if self.board_properties["name"] is "":
			raise ConfigurationException("Board's name not valid")

	def set_agents_datas(self):
		self.agents_datas = self.parser.get_value_by_key("agents")

		if self.agents_datas == "":
			raise ConfigurationException("Agents's Node is not present !")

		for agent in self.agents_datas:
			if (not "name" in agent.keys()) or (not "pin_type" in agent.keys()) or (not "pin" in agent.keys()) or (not "pin_mode" in agent.keys()):
				raise ConfigurationException("One Agent's configuration missing some keys !")

			if agent["name"] is "" or agent["pin_type"] is "" or agent["pin"] is "" or agent["pin_mode"] is "" or (not int(agent["pin"])):
				raise ConfigurationException("One Agent's configuration is unvalid !")

	def set_composites_datas(self):
		self.composite_datas = self.parser.get_value_by_key("composites")

	@property
	def is_loaded(self):
		return self.json_file_loaded

	@property
	def mongo_datas(self):
		return self.mongo_properties

	@property
	def agents(self):
		return self.agents_datas

	@property 
	def board(self):
		return self.board_properties