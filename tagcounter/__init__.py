import logging
from .argument_handler import ArgumentHandler


def run():
    logging.basicConfig(
        level="INFO",
        filename="logs.log",
        format="%(asctime)s %(levelname)s %(message)s")

    handler = ArgumentHandler()
    handler.handle()
