from nanpy import *
from utils.logger import logger

class com_connexion(object):

	def is_available(show_log = False):
		try:
			ArduinoApi(SerialManager())
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