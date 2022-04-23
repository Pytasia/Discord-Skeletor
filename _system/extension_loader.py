import os


class extensions:
    def __init__(self, bot):
        self.bot = bot

    def load_system(self):
        for root, dirs, files in os.walk("_system_extensions", topdown=True):
            for name in files:
                file, extension = os.path.splitext(name)
                if extension == ".py":
                    self.bot.load_extension(root.replace(os.sep, ".") + "." + file)

    def load_plugins(self):
        for root, dirs, files in os.walk("plugins", topdown=True):
            for name in files:
                file, extension = os.path.splitext(name)
                if extension == ".py":
                    self.bot.load_extension(root.replace(os.sep, ".") + "." + file)





