from src.webservice.controller.webservice_controller import webservice_controller

class route_loader(object):

    def __init__(self, _app, mongo_datas):
        self.ws_controller = webservice_controller(mongo_datas);
        self.app = _app

    def load_all_route(self):
        self.app.route('/', callback=self.liste_boards)
        self.app.route('/<boardname>', callback=self.liste_agents)
        self.app.route('/<boardname>/<agentname>/write', method="POST", callback=self.write)
        self.app.route('/<boardname>/<agentname>/read', callback=self.valeur_agent)
        self.app.route('/<boardname>/<agentname>/read/last/<number:int>', callback=self.last_value_agent)
        self.app.route('/<boardname>/<agentname>/read/first/<number:int>', callback=self.first_value_agent)

    def liste_boards(self):
        return self.ws_controller.get_boards()

    def liste_agents(self, boardname):
        return self.ws_controller.get_agents(boardname)

    def write(self, boardname, agentname):
        return self.ws_controller.post_value_in(boardname,agentname)

    def valeur_agent(self, boardname, agentname):
        return self.ws_controller.get_value_in(boardname,agentname)

    def last_value_agent(self, boardname, agentname, number):
        return self.ws_controller.get_number_of_last_value_in(boardname,agentname,number)

    def first_value_agent(self, boardname, agentname, number):
        return self.ws_controller.get_number_of_first_value_in(boardname,agentname,number)