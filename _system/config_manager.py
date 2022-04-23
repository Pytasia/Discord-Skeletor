import os
from configparser import ConfigParser


class config:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(os.path.join(os.path.abspath("assets"), "config.ini"))

    def bot_config(self, value):
        config = self.config["BOT"][value]
        return config

    def mysql_config(self):
        db = self.config._sections['MYSQL']
        return db

    def settings(self):
        settings = self.config._sections['SETTINGS']
        return settings


