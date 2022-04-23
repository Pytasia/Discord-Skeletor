from datetime import datetime
import os

import discord
from discord import guild
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from _system import config_manager, extension_loader, output_manager

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = config_manager.config()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.config.settings()['user_welcome_msg'] == 'True':
            await member.guild.system_channel.send(output_manager.output().output_notification('user_welcome_msg').format(user=member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if self.config.settings()['user_leave_msg'] == 'True':
            await member.guild.system_channel.send(output_manager.output().output_notification('user_leave_msg').format(user=member))


def setup(bot):
    bot.add_cog(user(bot))
    print(output_manager.output().output_notification('loaded_plugin').format(plugin_name=__name__))
