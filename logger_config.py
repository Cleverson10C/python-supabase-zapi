import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("app.log"),  # salva em arquivo
            logging.StreamHandler()          # mostra no console
        ]
    )
    return logging.getLogger(__name__)
