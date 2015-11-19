from src.webservice.model.warehouse import warehouse
import json

class webservice_controller(object):

        def __init__(self, mongo_datas):
            self.warehouse = warehouse(mongo_datas);

        def to_json(self, array):
            return json.dumps(array)

        def get_boards(self):
            return self.to_json(self.warehouse.get_list_boards())

        def get_agents(self, boardname):
             return self.to_json(self.warehouse.get_list_agents(boardname))

