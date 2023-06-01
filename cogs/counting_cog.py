from datetime import datetime, timedelta

import discord
from discord.ext import commands


class CountingCog(commands.Cog):
    def __init__(self,
                 bot: discord.Bot,
                 counting_config: dict):
        self.bot = bot
        self.counting_config = counting_config

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if self.counting_config:
            counting_fail_role_id = self.counting_config.get('counting-fail-role-id')
            if counting_fail_role_id and len(before.roles) < len(after.roles):
                new_role = next(role for role in after.roles if role not in before.roles)
                if new_role and new_role.id == self.counting_config.get('counting-fail-role-id'):
                    timeout_minutes = self.counting_config.get('time-out-minutes', 5)
                    expiration_date_time = datetime.utcnow() + timedelta(
                        minutes=timeout_minutes)
                    timeout_text = self.counting_config.get("time-out-text",
                                                            "You failed the counting bot so you get a timeout!")
                    await after.timeout(until=expiration_date_time, reason=timeout_text)
                    print(f"{after.name} failed the counting bot and got a time of {timeout_minutes}!")
