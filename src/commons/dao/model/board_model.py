from ..driver.mongo_driver import mongo_driver

class board_model(object):
	def __init__(self, mongo_data):
		self.mongo_client = mongo_driver(mongo_data)
		self.db = self.mongo_client.db

	def flush_collection(self, board_name):
		self.db[board_name].remove()

	@property
	def connection_established(self):
		return self.mongo_client.connected