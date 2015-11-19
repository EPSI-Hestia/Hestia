class route_loader(object):

    def __init__(self,_app, p_nom):
        self.nom = p_nom
        self.app =  _app

    def load_all_route(self):
        self.app.route('/<boards>', callback=self.liste_boards)
        self.app.route('/<boardname>', callback=self.liste_agents)
        self.app.route('/<boardname>/<agentname>/write/<value>', callback=self.write)
        self.app.route('/<boardname>/<agentname>/read', callback=self.valeur_agent)
        self.app.route('/<boardname>/<agentname>/read/last/<number:int>', callback=self.last_value_agent)
        self.app.route('/<boardname>/<agentname>/read/first/<number:int>', callback=self.first_value_agent)

    def liste_boards(self):
        return "liste des agents :"

    def liste_agents(self, boardname):
        return boardname

    def write(self, boardname, agentname, value):
        return agentname

    def valeur_agent(self, boardname, agentname):
        return boardname

    def last_value_agent(self, boardname, agentname, number):
        return boardname

    def first_value_agent(self, boardname, agentname, number):
        return boardname