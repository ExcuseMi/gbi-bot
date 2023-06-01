Create a discord bot to get a discord token for the bot: https://www.writebots.com/discord-bot-token/

Invite it to your discord with all permissions.

https://discord.com/api/oauth2/authorize?client_id=<client_id>&permissions=8&scope=bot%20applications.commands

Replace the client_id with the one from the bot.

Copy config-example.json to config.json and add the discord-token from your bot.

Edit the config.json to your liking.

Import the dependencies using the command: python -m pip -r requirements.txt

Run the bot via the command: python bot.py