import yaml
import lib.config.Config as Config


class Yaml(Config):
    def __init__(self, file):
        with open(file, 'r') as yamlfile:
            self._cfg = yaml.load(yamlfile)