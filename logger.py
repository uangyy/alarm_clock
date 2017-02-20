import logging

ch = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s - %(name)s, line %(lineno)d][%(levelname)s]: %(message)s')
ch.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(ch)
