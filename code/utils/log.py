import logging
import os

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s : %(message)s', 
                    filename=os.path.join(__file__, os.pardir, os.pardir, 'work.log'))
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s : %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)