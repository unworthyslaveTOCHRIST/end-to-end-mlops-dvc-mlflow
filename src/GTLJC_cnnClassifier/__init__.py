# ALL THANKS AND GLORY TO THE AND my ONLY GOD AND LORD JESUS CHRIST ALONE

import os
import sys
import logging

GTLJC_logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

GTLJC_log_dir = "logs"
GTLJC_log_filepath = os.path.join(GTLJC_log_dir, "running_logs.log")

os.makedirs(GTLJC_log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format = GTLJC_logging_str,

    handlers = [
        logging.FileHandler(GTLJC_log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

GTLJC_logger = logging.getLogger("cnnClassifierLogger")