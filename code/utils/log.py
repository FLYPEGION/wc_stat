import logging
import os

FORMAT = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
file_handler = logging.FileHandler(filename=os.path.join(__file__, os.pardir, os.pardir, 'work.log'), 
                                    encoding='utf-8', mode='a+')
stream_handler = logging.StreamHandler()
file_handler.setFormatter(FORMAT)
stream_handler.setFormatter(FORMAT)
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)