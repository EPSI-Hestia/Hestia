from src.server.server.server_core import server_core
from src.commons.utils.logger import logger

import sys

if __name__ == "__main__":
	args = sys.argv[1:]

	try:
		if len(args) >= 2:
			logger.set_level(args[1])
		elif len(args) <= 0:
			logger.error("[MAIN] Please add configuration file path to launch command parameters")

		server = server_core(args[0])

		logger.info("Bye !")
	except:
		logger.error("[CRITICAL_ERROR] Hestia is stoping !]")
		exit(1)

	exit(0)