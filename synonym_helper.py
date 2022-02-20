import yaml


class SynonymHelper:
    DEFAULT_FILE_NAME = "synonyms.yaml"

    @classmethod
    def read(cls, synonym):
        with open(cls.DEFAULT_FILE_NAME, "r") as file:
            cur_yaml = yaml.safe_load(file)
        return cur_yaml[synonym]

    @classmethod
    def write(cls, synonym, site_name):
        with open(cls.DEFAULT_FILE_NAME, 'r') as file:
            cur_yaml = yaml.safe_load(file)

        cur_yaml[synonym] = site_name if cur_yaml is not None else dict({synonym: site_name})

        with open(cls.DEFAULT_FILE_NAME, 'w') as file:
            yaml.safe_dump(cur_yaml, file)

    @classmethod
    def remove(cls, synonym):
        with open(cls.DEFAULT_FILE_NAME, "r") as file:
            cur_yaml = yaml.safe_load(file)
            del cur_yaml[synonym]

        with open(cls.DEFAULT_FILE_NAME, 'w') as file:
            yaml.safe_dump(cur_yaml, file)
