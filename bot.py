import json
import discord
from cogs.counting_cog import CountingCog

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE) as f:
    CONFIG = json.load(f)


class BasicBot(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.reactions = True
bot = BasicBot(intents=intents)
token = CONFIG.COUNTING_COFIG('discord-token')
COUNTING_CONFIG = CONFIG.get('counting', {})
if COUNTING_CONFIG:
    bot.add_cog(CountingCog(bot, COUNTING_CONFIG))
if token:
    bot.run(token, reconnect=True)
else:
    print("No discord-token provided!")