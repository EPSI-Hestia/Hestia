from src.server.agents.analogic.analogic_agent import analogic_agent

class light_agent(analogic_agent):
	def __init__(self,  agent_data):
		analogic_agent.__init__( self, agent_data)

	def convert_volt_to_lux(self, value_to_convert):
		return value_to_convert

	def value(self):
		value_read = self.pin.read()
		value_to_return = ""

		if value_read is not None and value_read != "":
			value_to_return = str(self.convert_volt_to_lux(value_read))

		return value_to_return
