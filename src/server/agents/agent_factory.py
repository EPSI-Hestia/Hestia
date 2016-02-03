from src.server.agents.analogic.light_agent import light_agent
from src.server.agents.analogic.temp_agent import temp_agent
from src.server.agents.digital.digital_agent import digital_agent
from src.server.agents.analogic.generic_analogic_agent import generic_analogic_agent

class agent_factory(object):
    def create(agent_data):
    	name =  agent_data['name'].lower()
        if "light_agent" in name: return light_agent(agent_data)
        if "temp_agent" in name: return temp_agent(agent_data)
        if "digital_agent" in name: return digital_agent(agent_data)
        if "analogic" in name : return generic_analogic_agent(agent_data)

    create = staticmethod(create)