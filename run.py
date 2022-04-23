import discord
from discord.ext import commands
from discord_slash import SlashCommand

from _system import config_manager, extension_loader, output_manager


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guilds = []
        for guild in self.bot.guilds:
            guilds.append(guild.name)

        extension_loader.extensions(self.bot).load_system()
        extension_loader.extensions(self.bot).load_plugins()
        start_active_guilds = output_manager.output().output_notification('start_active_guilds').format(guilds=guilds)
        start_text = output_manager.output().output_notification('start_bot').format(botname=self.bot.user.name)

        # Output
        print(start_active_guilds)
        print(start_text)


config = config_manager.config()
bot = commands.Bot(command_prefix=config.bot_config('prefix'),
                   help_command=None,
                   case_insensitive=True,
                   intents=discord.Intents.all()
                   )

if (config.settings()['using_slash_commands']) == 'True':
    slash = SlashCommand(bot, sync_commands=True)

if __name__ == "__main__":
    bot.add_cog(main(bot))
    bot.run(config.bot_config('token'), bot=True, reconnect=True)
