import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLog(self):
        loggerName = inspect.stack()[1][3]  # Gets the name of the class / method from where this method is called
        logger = logging.getLogger(loggerName)
        # formatter will produce...201-19-02-17 12:40:14,798 : ERROR: <testcasename>: Fatal error in submitting credit card payment on step 4. Cannot continue...using for formatting error logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger