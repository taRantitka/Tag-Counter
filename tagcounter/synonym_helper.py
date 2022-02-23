import yaml
import os


class SynonymHelper:
    DEFAULT_FILE_NAME = "synonyms.yaml"

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), self.DEFAULT_FILE_NAME)

    def read(self, synonym):
        with open(self.file_path, "r") as file:
            cur_yaml = yaml.safe_load(file)
        return cur_yaml.get(synonym)

    def write(self, synonym, site_name):
        with open(self.file_path, 'r') as file:
            cur_yaml = yaml.safe_load(file)

        cur_yaml[synonym] = site_name if cur_yaml is not None else dict({synonym: site_name})

        with open(self.file_path, 'w') as file:
            yaml.safe_dump(cur_yaml, file)

    def remove(self, synonym):
        with open(self.file_path, "r") as file:
            cur_yaml = yaml.safe_load(file)
            del cur_yaml[synonym]

        with open(self.file_path, 'w') as file:
            yaml.safe_dump(cur_yaml, file)
