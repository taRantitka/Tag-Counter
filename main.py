from argument_handler import ArgumentHandler
import logging


def main():
    handler = ArgumentHandler()
    handler.handle()


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs.log",
        level="INFO",
        format="%(asctime)s %(levelname)s %(message)s")
    main()
