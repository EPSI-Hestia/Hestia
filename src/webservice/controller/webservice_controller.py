from src.commons.dao.model.agent_model import agent_model
from src.commons.dao.model.board_model import board_model
from bottle import response, request
import json

class webservice_controller(object):

        def __init__(self, mongo_datas):
            self._mongo_datas = mongo_datas

        def to_json(self, array):
            response.content_type = 'application/json'
            return json.dumps(array)

        def get_boards(self):
            self.board_model = board_model(self._mongo_datas)
            return self.to_json(self.board_model.get_list_boards())

        def get_agents(self, boardname):
            self.board_model = board_model(self._mongo_datas)
            return self.to_json(self.board_model.get_list_agents(boardname))

        def get_value_in(self, boardname, agentname):
            self.agent_model = agent_model(self._mongo_datas, boardname, agentname)
            return self.to_json(self.agent_model.get_last_entry_value_and_date())

        def get_number_of_last_value_in(self, boardname, agentname, number):
            self.agent_model = agent_model(self._mongo_datas, boardname, agentname)
            return self.to_json(self.agent_model.get_last_entries(number))

        def get_number_of_first_value_in(self,boardname, agentname, number):
            self.agent_model = agent_model(self._mongo_datas, boardname, agentname)
            return self.to_json(self.agent_model.get_first_entries(number))

        def post_value_in(self,boardname, agentname):
            self.agent_model = agent_model(self._mongo_datas, boardname, agentname)
            value = request.forms.get('value')
            return self.to_json(self.agent_model.insert(value))