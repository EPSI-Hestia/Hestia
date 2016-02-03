from src.commons.dao.driver.mongo_driver import mongo_driver

class board_model(object):
	def __init__(self, mongo_data):
		self.mongo_client = mongo_driver(mongo_data)
		self.db = self.mongo_client.db

	def flush_collection(self, board_name):
		self.db[board_name].remove()

	def get_list_boards(self):
		boards_list = self.db.collection_names(include_system_collections=False)
		boards = []
		for board in boards_list:
			if '.agents' in board:
				boards.append(board.split(".")[0])
		return boards

	def get_list_agents(self, boardname):
		agents_list = self.db[boardname]["agents"].distinct('name')
		return agents_list

	def remove_agent_data(self, boardname, agent_name):
		self.db[boardname]["agents"].remove({"name" : agent_name})

	@property
	def connection_established(self):
		return self.mongo_client.connected