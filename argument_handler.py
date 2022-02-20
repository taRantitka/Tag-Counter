import argparse
from scraper import Scraper
from data_access import DataAccess
from synonym_helper import SynonymHelper

class ArgumentHandler:

    APP_NAME = "tagcounter"

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("app_name")
        self.parser.add_argument("--get", nargs=1)
        self.parser.add_argument("--view", nargs=1)

    def handle(self):
        args = self.parser.parse_args()


        if args.app_name == self.APP_NAME:

            if args.get is not None:
                Scraper.scrape(args.get[0])
            elif args.view is not None:

                SynonymHelper.remove("hhh")
                #print(DataAccess().get(args.view[0]))
        else:
            pass