from datetime import datetime
import os

import discord
from discord import guild
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from _system import config_manager, extension_loader, output_manager


class error_logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def write_log(self, server, action, context):
        log_path = "logs/system"
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        f = open(os.path.join(os.path.join(os.path.abspath(""), log_path, server + ".log")), "a")

        f.write(
            "{0} - {2} - {1} - {3}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), action, server, context))
        f.close()


class user_logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def check_log(self):
        self.config = config_manager.config()
        log_var = self.config.settings()['using_logs']
        if log_var == 'True':
            return True
        else:
            return False

    def write_log(self, server, action, context):
        log_path = "logs"
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        f = open(os.path.join(os.path.join(os.path.abspath(""), log_path, server + ".log")), "a")

        f.write(
            "{0} - {2} - {1} - {3}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), action, server, context))
        f.close()


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if self.check_log():
            self.write_log(message.guild.name, "DELETE MSG" + message.author.name, message.channel.name + message.content)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        if self.check_log():
            self.write_log(guild.name, user.name + "BAN", f"{user.name}")


    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        if self.check_log():
            self.write_log(guild.name, user.name + "KICK", f"{user.name}")

def setup(bot):
    bot.add_cog(error_logger(bot))
    bot.add_cog(user_logger(bot))
    print(output_manager.output().output_notification('loaded_plugin').format(plugin_name=__name__))
