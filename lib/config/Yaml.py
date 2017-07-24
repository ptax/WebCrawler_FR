import yaml
import lib.config.Config as Config


class Yaml(Config):
    def __init__(self, file_name):
        with open(file_name, 'r') as yamlfile:
            self._cfg = yaml.load(yamlfile)