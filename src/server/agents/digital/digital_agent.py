from agents.agents import agents

class digital_agent(agents):
	def __init__(self, agent_data):
		self.cpt = 0
		agents.__init__(self, agent_data)

	def value(self):
		value_read = self.pin.read()
		value_to_return = ""

		if value_read is not None and value_read != "":
			value_to_return = str(value_read)

		return value_to_return