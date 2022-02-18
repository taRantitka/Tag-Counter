from argument_handler import ArgumentHandler
import argparse
import logging
from scraper import Scraper
from data_access import DataAccess


def main():
    handler = ArgumentHandler()
    handler.handle()

    #Scraper().scrape("https://stackoverflow.com/questions/5260095/saving-tuples-as-blob-data-types-in-sqlite3-in-python/25763101")
    #da = DataAccess()
    #da.generate()
    #print(da.get("stackoverflow.com"))


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs.log",
        level="INFO",
        format="%(asctime)s %(levelname)s %(message)s")
    main()