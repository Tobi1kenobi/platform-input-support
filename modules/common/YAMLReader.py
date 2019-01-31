import logging
import yaml
from addict import Dict
from definitions import ROOT_DIR

logger = logging.getLogger(__name__)


class YAMLReader(object):

    def __init__(self, yaml_file=ROOT_DIR+'/'+'config.yaml' ):
        self.yaml_file = yaml_file
        self.yaml_dictionary = {}

    def get_Dict(self):
        with open(self.yaml_file, 'r') as stream:
            try:
                self.yaml_dictionary = Dict(yaml.load(stream))
            except yaml.YAMLError as exc:
                print(exc)
        return self.yaml_dictionary

    def get_list_keys(self):
        return self.yaml_dictionary.keys()
