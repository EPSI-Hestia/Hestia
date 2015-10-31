from .analogic_agent import analogic_agent

from math import log

class temp_agent(analogic_agent):
	def __init__(self,  agent_data):
		analogic_agent.__init__( self,  agent_data)

	def convert_volt_to_celsius(self, value_to_convert):
		if(value_to_convert > 0):
			resistance= float(1023-value_to_convert)*10000/value_to_convert
			value_to_convert=1/(log(resistance/10000)/3975+1/298.15)-273.15
			value_to_convert = round(value_to_convert, 2)

		return value_to_convert

	def value(self):
		value_read = self.pin.read()
		value_to_return = ""

		if value_read is not None and value_read != "":
			value_to_return = str(self.convert_volt_to_celsius(value_read))

		return value_to_return