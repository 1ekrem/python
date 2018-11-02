import logging

# This will change the format of the log values.
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt = '%m-%d-%Y %I:%M:%S %p', level=logging.DEBUG) 
logging.warning("warning message")
logging.info("info message")
logging.error("error message")