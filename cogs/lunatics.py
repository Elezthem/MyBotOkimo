import nextcord
from nextcord.ext import commands
from nextcord.utils import sleep_until
from datetime import datetime, timezone, timedelta
from collections import defaultdict


# время указано в UTC
START_HOUR = 19
END_HOUR = 2

GUILD_ID = 900349173029806110
ROLE_ID = 935934427572342894
MESSAGES_NEEDED = 5
IGNORE_ROLE = 900416072539328532


class Lunatics(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.users = defaultdict(int)
        self.bot = bot
        bot.loop.create_task(self.remove_roles())

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if getattr(message.guild, "id", None) != GUILD_ID or message.author.bot:
            return
        if message.guild.get_role(IGNORE_ROLE) in message.author.roles:
            return
        hour = datetime.now(timezone.utc).hour
        if hour < START_HOUR and hour >= END_HOUR:
            return

        self.users[message.author.id] += 1
        if self.users[message.author.id] == MESSAGES_NEEDED:
            try:
                await message.author.add_roles(
                    message.guild.get_role(ROLE_ID), reason="актив ночью"
                )
            except Exception:
                pass

    async def remove_roles(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.now(timezone.utc)
            if now.hour >= START_HOUR:
                now += timedelta(1)
            next = datetime(
                now.year, now.month, now.day, START_HOUR, tzinfo=timezone.utc
            )
            print("Следующее обнуление лунатиков будет", next)
            await sleep_until(next)
            guild = self.bot.get_guild(GUILD_ID)
            role = guild.get_role(ROLE_ID)
            ignore = guild.get_role(IGNORE_ROLE)
            for member in role.members:
                if ignore not in member.roles:
                    try:
                        await member.remove_roles(role, reason="ежедневный сброс")
                    except Exception:
                        pass
            print("Лунатики обнулены.")


def setup(bot):
    bot.add_cog(Lunatics(bot))
