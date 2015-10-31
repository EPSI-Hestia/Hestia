from ..driver.mongo_driver import mongo_driver
import datetime
import pymongo

class agent_model(object):
	def __init__(self, mongo_data, board_name, _agent_name):
		self.mongo_client = mongo_driver(mongo_data)
		self.db = self.mongo_client.db
		self.collection = self.db[board_name]["agents"]
		#self.collection.remove()
		self.agent_name = _agent_name

	def insert(self, value):
		self.collection.insert({"name" : self.agent_name, "value" : value, "datetime" : datetime.datetime.utcnow(), "mode" : "w"})

	def get_last_entry(self):
		last_entry = self.collection.find_one({"name" : self.agent_name}, sort=[("datetime", pymongo.DESCENDING)])

		# In case of db is empty
		if last_entry is None:
			last_entry = {}
			last_entry["mode"] = "w"

		return last_entry