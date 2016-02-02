from src.commons.utils.pin import *
from src.commons.utils.logger import logger

import sys
import glob
import serial

class com_connexion(object):

	def serial_ports(name="toto"):
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = glob.glob('/dev/tty*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*usbmodem*')
		else:
			raise EnvironmentError('Unsupported platform')

		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)

			except (OSError, serial.SerialException):
				pass

		return result

	def is_available(show_log = False):
		'''connexion_established = True

		try:
		witness_led = pin("13", "OUTPUT", "digital")
		witness_led.write("1")

		connexion_established = (str(witness_led.read()) == "1")

		if(connexion_established):
			witness_led.write("0")

		connexion_established = (str(witness_led.read()) == "0")
		#except:
		#	connexion_established = False

		if not connexion_established:
			logger.error("Connexion failed while trying to connect")
		'''
		return True

	is_available = staticmethod(is_available)
	serial_ports = staticmethod(serial_ports)
