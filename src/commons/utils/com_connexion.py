from nanpy import *
from src.commons.utils.logger import logger
import sys
import glob
import serial

class com_connexion(object):

	def serial_ports(name="toto"):
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')
		else:
			raise EnvironmentError('Unsupported platform')

		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()

				if "usbmodem" in port:
					result.append(port)
			except (OSError, serial.SerialException):
				pass

		return result

	def is_available(show_log = False):
		try:
			ArduinoApi(SerialManager(com_connexion.serial_ports()[0]))
			connexion_established = True

			if show_log:
				logger.info("Board available")
		except:
			connexion_established = False

		if not connexion_established:
			logger.error("Board is not available")
			print "Board is not available"

		return connexion_established

	is_available = staticmethod(is_available)
	serial_ports = staticmethod(serial_ports)
