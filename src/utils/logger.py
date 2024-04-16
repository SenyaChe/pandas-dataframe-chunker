import logging


def setup_logging():
    # Configure the basic settings for logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )


setup_logging()
