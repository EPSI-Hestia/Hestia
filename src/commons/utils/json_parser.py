from src.commons.utils.logger import logger
from PyQt4.QtCore import QString
import json
import os

class json_parser(object):
	def __init__(self, json_configuration_file):
		self.config_file = json_configuration_file
		self.init_attr()

	def init_attr(self):
		self.open_file_and_get_datas()

	def open_file_and_get_datas(self):
		try:
			with open(self.config_file) as data_file:
					self.datas = json.load(data_file)
		except:
			logger.error("[JSON_PARSER] fail to opening %s check the file" % self.config_file)

	def get_value_by_key(self, key):
		return_value = ""

		try:
			return_value = self.datas[key]
		except Exception, e:
			logger.error("while parsing json file")

		return return_value

	def check_if_file_exists_and_its_valid_json(self):
		is_valid = False

		if isinstance(self.config_file, QString):
			self.config_file = str(self.config_file)
		elif self.config_file is None:
			self.config_file = ""

		if os.path.isfile(self.config_file) and self.config_file.endswith(".json"):
			is_valid = True

		return is_valid

