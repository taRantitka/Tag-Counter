import argparse
from .scraper import Scraper
from .data_access import DataAccess
from .gui_client import GUIClient
from .synonym_helper import SynonymHelper


class ArgumentHandler:
    APP_NAME = "tagcounter"

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("app_name", help="application name")
        self.parser.add_argument("--get", nargs=1, help="scrap tags")
        self.parser.add_argument("--view", nargs=1, help="view tags")
        self.parser.add_argument("--ads", nargs=2, help="add synonym")
        self.parser.add_argument("--rms", nargs=1, help="remove synonym")
        self.parser.add_argument("--gen", action='store_true', help="generate database")

    def handle(self):
        args = self.parser.parse_args()

        if args.app_name == self.APP_NAME:

            if args.get:
                print(Scraper.scrape(args.get[0]))
            elif args.view:
                print(DataAccess().get(args.view[0]))
            elif args.ads:
                SynonymHelper().write(args.ads[0], args.ads[1])
            elif args.rms:
                SynonymHelper().remove(args.rms[0])
            elif args.gen:
                SynonymHelper().remove(args.rms[0])
            else:
                GUIClient()
        else:
            self.parser.print_help()
