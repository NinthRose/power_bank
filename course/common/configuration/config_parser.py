import configparser
import os

from course import base_dir


class OrcaConfig():
    def __init__(self):
        self.update()

    def update(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(base_dir, 'config.cfg')
        self.config.read(config_path, encoding='utf8')

    def get_config(self, section, option, type=None):
        if not type:
            return self.config.get(section, option)
        if issubclass(type, int):
            return self.config.getint(section, option)
        elif issubclass(type, float):
            return self.config.getfloat(section, option)
        elif issubclass(type, bool):
            return self.config.getboolean(section, option)
        elif issubclass(type, dict):
            return self.config.items(section)
        elif issubclass(type, str):
            return self.config.get(section, option)


power_config = OrcaConfig()
