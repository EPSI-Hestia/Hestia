import datetime

class logger(object):
    level = 0
    monitoring_entry_counter = 0
    monitoring_number_of_entries_to_skip = 10

    @staticmethod
    def log(message):
        print(str(datetime.datetime.utcnow().strftime('%d/%m/%Y - %H:%M:%S')) + " - " + message)

    @staticmethod
    def info(message):
        logger.log("INFO : " + message)

    @staticmethod
    def error(message):
        if logger.level > 0:
            logger.log("ERROR : %s" % message)

    @staticmethod
    def event(message):
        if logger.level > 1:
            logger.log("=> EVENT : " + message)

    @staticmethod
    def monitoring(message):
        if logger.level > 2:
            logger.monitoring_entry_counter += 1

            if logger.monitoring_entry_counter >= logger.monitoring_number_of_entries_to_skip:
                logger.log("MONITOR : " + message)
                logger.monitoring_entry_counter = 0

    @staticmethod
    def set_level(_level):
        logger.level = _level