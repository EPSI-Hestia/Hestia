from src.commons.dao.driver.mongo_driver import mongo_driver

class warehouse(object):

    def __init__(self, mongo_connexion):
        self.agents_exist = False
        self.mongo_client = mongo_driver(mongo_connexion)
        self.db = self.mongo_client.db


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

