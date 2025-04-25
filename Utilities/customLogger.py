import logging
import datetime

class LogGen:

    @staticmethod
    def loggen():
        #timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")
        logger=logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
