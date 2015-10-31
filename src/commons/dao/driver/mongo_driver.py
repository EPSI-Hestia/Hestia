from pymongo import *
from utils.logger import logger

class mongo_driver(object):

	def __init__(self, datas):
		self.set_attr(datas)

	def __del__(self):
		if self.client:
			self.client.close()

	def set_attr(self, datas):
		self.conexion_available = True

		credentials_string = 'mongodb://' + datas["mongo_user"] + ':' + datas["mongo_pwd"] + '@' + datas["mongo_host"] + ':' + str(datas["mongo_port"]) + '/' + datas["mongo_db"]

		try:
			self.client = MongoClient(credentials_string)
			self.db_connection = self.client[datas["mongo_db"]]
		except:
			logger.error("[MONGO_DRIVER] Mongo db connection fail !")
			self.conexion_available = False

	@property
	def db(self):
		return self.db_connection

	@property
	def connected(self):
		return self.conexion_available
