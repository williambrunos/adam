import logging


def setup_logger():
    # Configure the root logger
    logging.basicConfig(level=logging.INFO)

    # Create and configure a custom logger
    logger = logging.getLogger("web_scraper")
    logger.setLevel(logging.INFO)

    # Create a console handler and set the level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger
