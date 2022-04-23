import os
from configparser import ConfigParser
from _system import config_manager


class output:
    def __init__(self):
        self.output = ConfigParser()
        self.output.read(os.path.join(os.path.abspath("assets/lang"), config_manager.config().bot_config('lang') + ".ini"))

    def output_error(self, value):
        output = self.output["ERROR"][value]
        return output

    def output_notification(self, value):
        output = self.output["NOTIFICATION"][value]
        return output





