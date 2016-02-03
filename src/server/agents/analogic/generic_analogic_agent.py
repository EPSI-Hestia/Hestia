from src.server.agents.analogic.analogic_agent import analogic_agent

class generic_analogic_agent(analogic_agent):
	def __init__(self,  agent_data):
		analogic_agent.__init__( self, agent_data)

	def value(self):
		return self.pin.read()
