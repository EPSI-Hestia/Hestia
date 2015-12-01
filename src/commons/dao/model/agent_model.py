from src.commons.dao.driver.mongo_driver import mongo_driver
import datetime
import pymongo

class agent_model(object):
	def __init__(self, mongo_data, board_name, _agent_name):
		self.mongo_client = mongo_driver(mongo_data)
		self.db = self.mongo_client.db
		self.collection = self.db[board_name]["agents"]
		#self.collection.remove()
		self.agent_name = _agent_name

	def insert(self, value, mode = False):
		if mode :
			writting_mode = "r"
		else:
			writting_mode = "w"

		self.collection.insert({"name" : self.agent_name, "value" : value, "datetime" : datetime.datetime.utcnow(), "mode" : writting_mode})

	def get_last_entry(self):
		last_entry = self.collection.find_one({"name" : self.agent_name}, sort=[("datetime", pymongo.DESCENDING)])

		# In case of db is empty
		if last_entry is None:
			last_entry = {}
			last_entry["mode"] = "w"

		return last_entry

	def get_last_entry_value_and_date(self):
		last_entry = self.collection.find_one({"name" : self.agent_name}, sort=[("datetime", pymongo.DESCENDING)])

		datas = {}
		if last_entry is not None:
			datas["value"] = last_entry["value"]
			datas["datetime"] = last_entry["datetime"].strftime('%d/%m/%Y - %H:%M:%S')
			datas["mode"] = last_entry["mode"]

		return datas

	def get_last_entries(self, number_of_entries):
		last_number_values = self.collection.find({"name" : self.agent_name}).limit(number_of_entries).sort("datetime", -1)

		values = []
		for last_number_value in last_number_values:
			entry = {}
			entry["value"] = last_number_value["value"]
			entry["datetime"] = last_number_value["datetime"].strftime('%d/%m/%Y - %H:%M:%S')
			entry["mode"] = last_number_value["mode"]

			values.append(entry)

		return values

	def get_first_entries(self, number_of_entries):
		first_number_values = self.collection.find({"name" : self.agent_name}).limit(number_of_entries).sort("datetime", 1)

		values = []
		for first_number_value in first_number_values:
			entry = {}
			entry["value"] = first_number_value["value"]
			entry["datetime"] = first_number_value["datetime"].strftime('%d/%m/%Y - %H:%M:%S')
			entry["mode"] = first_number_value["mode"]

			values.append(entry)

		return values

