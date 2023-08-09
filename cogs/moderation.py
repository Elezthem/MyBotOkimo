# Настройка
import nextcord
from nextcord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        if reason is None:
            reason == "Без причины"
        await member.ban(reason=reason)
        emb = nextcord.Embed(
            title="Пользователь забанен",
            description=f"Пользователь {member.mention} был забанен на сервере {ctx.guild.name} модератором {ctx.author.mention} по причине {reason}",
            timestamp=ctx.message.created_at,
            color=nextcord.Color.blue(),
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        if reason is None:
            reason == "Без причины"
        await member.kick()
        emb = nextcord.Embed(
            title="Пользователь кикнут",
            description=f"Пользователь {member.mention} был кинут на сервере {ctx.guild.name} модератором {ctx.author.mention} по причине {reason}",
            timestamp=ctx.message.created_at,
            color=nextcord.Color.blue(),
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=20):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Очищено {amount} сообщений модератором {ctx.author.mention}")


def setup(bot):
    bot.add_cog(Moderation(bot))
