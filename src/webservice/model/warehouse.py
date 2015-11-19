from src.commons.dao.driver.mongo_driver import mongo_driver

class warehouse(object):

    def __init__(self, mongo_connexion):
        self.agents_exist = False
        self.mongo_client = mongo_driver(mongo_connexion)
        self.db = self.mongo_client.db


    def get_list_boards(self):
        collection_list = self.db.collection_names(include_system_collections=False)
        boards = []
        for collection in collection_list:
            if '.agents' in collection:
                boards.append(collection.split(".")[0])
        return boards

    def get_list_agents(self):
        agents = []
        return agents

