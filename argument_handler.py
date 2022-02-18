import argparse


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
                print("GET")
            elif args.view is not None:
                print("VIEW")
        else:
            self.parser.print_help()
