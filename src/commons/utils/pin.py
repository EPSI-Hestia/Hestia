from nanpy import *
from src.commons.utils.logger import logger

#TODO Refactring + import propre
class pin(object):

	def __init__(self, _pin_number, _pin_mode, _pin_type):
		self.pin_number = _pin_number
		self.pin_type = _pin_type
		self.arduino = ArduinoApi(SerialManager())

		if _pin_mode == "INPUT":
			mode = self.arduino.INPUT
		else:
			mode = self.arduino.OUTPUT

		self.arduino.pinMode(_pin_number, mode)

	def read(self):
		value_to_return = ""

		try:
			if self.pin_type == "digital":
				value_to_return = self.arduino.digitalRead(self.pin_number)
			elif self.pin_type == "analogic":
				value_to_return = self.arduino.analogRead(self.pin_number)
		except:
			logger.error("Arduino communication fail !")

		return value_to_return

	def write(self, value):
		try:
			if self.pin_type == "digital":
				if "1" in str(value):
					value = self.arduino.HIGH
				else:
					value = self.arduino.LOW
				self.arduino.digitalWrite(self.pin_number, value)
			elif self.pin_type == "analogic":
				self.arduino.analogWrite(self.pin_number, str(value))
		except:
			logger.error("Arduino communication fail !")
