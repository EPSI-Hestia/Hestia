from src.commons.dao.driver.mongo_driver import mongo_driver
import datetime
import pymongo

class warehouse(object):

    def __init__(self, mongo_data, board_name, _agent_name):
		self.mongo_client = mongo_driver(mongo_data)
		self.db = self.mongo_client.db
		self.collection = self.db[board_name]["agents"]
		self.agent_name = _agent_name


    def get_last_entry(self):
        last_entry = self.collection.find_one({"name" : self.agent_name}, sort=[("datetime", pymongo.DESCENDING)])
        if last_entry is None:
                last_entry = {}
                last_entry["mode"] = "w"

        return last_entry

    def get_list_boards(self):
        return self.db._list_collections()