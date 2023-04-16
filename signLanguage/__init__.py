import os.path
import sys
import yaml
import base64

from signLanguage.exception import SignException
from signLanguage.logger import Logger import logging

def read_yaml_file(filename):