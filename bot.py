from asyncio import streams
from audioop import add
from cgitb import text
from http import client
from lib2to3.pgen2 import token
from optparse import Option
from pydoc import describe
from sqlite3 import connect
from token import SLASH
from tokenize import maybe

from typing import Any
from unicodedata import name
from urllib import response
from webbrowser import get
from nextcord import Interaction
import nextcord
from nextcord.ext import commands

from modules.components import HelpCommandView
from modules.utils import maybe_delete
from nextcord.utils import utcnow
from nextcord.utils import get
from translate import Translator
import os
import random
import requests
from PIL import Image, ImageFont, ImageDraw
import youtube_dl
import time
import timeago as timesince
import datetime
import calendar
start_time = utcnow()


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")

@bot.command()
async def embed(ctx, *, content: str):
    await ctx.channel.purge(limit=1)
    title, description = content.split("|")
    embed = nextcord.Embed(
        title=title,
        description=description,
        color=nextcord.Color.blue(),
        timestamp=ctx.message.created_at,
    )
    await ctx.send(embed=embed)

def some_function():
    "This function does nothing"
    return None


def date(
    target,
    clock: bool = True,
    seconds: bool = False,
    ago: bool = False,
    only_ago: bool = False,
    raw: bool = False,
):
    if isinstance(target, int) or isinstance(target, float):
        target = datetime.datetime.utcfromtimestamp(target)

    if raw:
        if clock:
            timestamp = target.strftime("%d %B %Y, %H:%M")
        elif seconds:
            timestamp = target.strftime("%d %B %Y, %H:%M:%S")
        else:
            timestamp = target.strftime("%d %B %Y")

        if isinstance(target, int) or isinstance(target, float):
            target = datetime.datetime.utcfromtimestamp(target)
            target = calendar.timegm(target.timetuple())

        if ago:
            timestamp += f" ({timesince.format(target)})"
        if only_ago:
            timestamp = timesince.format(target)

        return f"{timestamp} (UTC)"
    else:
        unix = int(time.mktime(target.timetuple()))
        timestamp = f"<t:{unix}:{'f' if clock else 'D'}>"
        if ago:
            timestamp += f" (<t:{unix}:R>)"
        if only_ago:
            timestamp = f"<t:{unix}:R>"
        return timestamp

@bot.command()
@commands.is_owner()
async def say(ctx, *, arg):
    await maybe_delete(ctx.message)
    await ctx.send(arg)


@bot.command()
async def help(ctx):
    view = HelpCommandView()
    await maybe_delete(ctx.message)
    emb = nextcord.Embed(
        title="Помощь по командам ➲",
        description="Все команды которые есть у меня. <:B_:1072106249103089684><:ET:1072106282015793235><:A_:1072106313062027304>",
        timestamp=ctx.message.created_at,
        color=nextcord.Color.blue(),
    )
    emb.add_field(
        name="> <:media:1097192443499266058> Сервер (BETA) ➲",
        value="`.embed` `.avatar` `.uptime` `.server` `.user`",
        inline=False,
    )
    emb.add_field(
        name="> <:student_cur:1097192375698337792> Информация (BETA) ➲",
        value="`.banner` `.uptime` `.avatar` `.helpserver` `.prefix`",
        inline=False,
    )
    emb.add_field(
        name="> <:pictures:1097192472670646352> Утилиты (BETA) ➲",
        value="`.embed` `.say` `.translate`",
        inline=False,
    )
    emb.add_field(
        name="> <:event:1097192407570849864> Развлечения (BETA) ➲",
        value="`.hello` `.megaping` `.ktoowner` `.norm` `.cho_delaesh` `.communicate` `.bye` `.xz` `.shapi` `.bob` `.tekashi69` `.morgen` `.bbt` `.kizaru` `.lilpump` `.lilpeep` `.falls` `.squirrel` `.tom` `.tsoy` `.skala` `.fox` `.wolf` `.xxxtentacion` `.trippie` `.rabbit` `.yzhik` `.kira` `.lilnasx` `.topic` `.tesla`",
        inline=False,
    )
    emb.add_field(
        name="> <:moon:1097192356865921084> Модерация (BETA) ➲",
        value="`.ban` `.kick` `.clear`",
        inline=False,
    )
    emb.add_field(
        name="> <:tribunemode:1097192458946887791> RolePlay (BETA) ➲",
        value="`.hug` `.slap` `.kiss` `.lewd` `.angry` `.kill` `.poke` `.pat` `.bite` `.feed` `.smile` `.lick` `.wave` `.yes` `.no` `.wink` `.cry` `.smug` `.cuddle` `.dance` `.sing` `.facepalm` `.jump` `.sip` `.yawn` `.shrug` `.drink` `.dab` `.nom` `.nosebleed` `.run` `.sleep` `.stare` `.laugh` `.yaoicuddle` `.yaoihug` `.yuricuddle` `.yurihug` `.yaoikiss` `.yeet` `.highfive` `.massage` `.marry` `.merkel` `.reward` `.squish` `.bonk` `.yurikiss` `.arrest` `.awkward` `.ghoul`",
        inline=False,
    )
    emb.add_field(
        name="> <:developer:1097192560696500234> Административное (BETA) ➲",
        value="`.embed` `.say` `.ping`",
        inline=False,
    )
    emb.add_field(
        name="> <:18yo:1097192487715606539> RolePLay 18+ (BETA) ➲",
        value="`.sixnine` `.assfuck` `.assgrab` `.blowjob` `.bondage` `.boobsgrab` `.boobsuck` `.creampie` `.cum` `.dickride` `.facesit` `.finger` `.footjob` `.fuck` `.furryfuck` `.handjob` `.leash` `.masturbate` `.pussyeat` `.spank` `.strip` `.tittyfuck` `.yaoifuck` `.yurifuck`",
        inline=False,
    )
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
    await ctx.send(content=ctx.author.mention, embed=emb, view=view)

@bot.command()
async def hello(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Привет! Как дела?")

@bot.slash_command(description="Сказать Акимочке 'Привет'")
async def hello(ctx):
    await ctx.send("Приветик! Как дыла?")

@bot.command()
async def ping(ctx):
    await maybe_delete(ctx.message)
    await ctx.send("@everyone")

@bot.slash_command(description="Упомянуть everyone")
async def ping(ctx):
    await ctx.send("||@everyone|| Мы без пингов!")

@bot.command()
async def ktoowner(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Мой создатель `Elezthem#7007` 🤍")

@bot.slash_command(description="Узнать кто мой разработчик")
async def ktoowner(ctx):
    await ctx.send("Мой создатель `Elezthem#7007` 🤍")

@bot.command()
async def megaping(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, mega-pong 🏓")

@bot.slash_command(description="Мега - понг")
async def megaping(ctx):
    await ctx.send("mega-pong 🏓")   

@bot.command()
async def norm(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Это хорошо, у меня тоже")

@bot.slash_command(description="Акимочке интересно какие у тебя дела)")
async def norm(ctx):
    await ctx.send("Великолепно! У меня дела нормальные")

@bot.command()
async def cho_delaesh(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Я жду пока мой хозяйн меня докодит) А ты?")

@bot.slash_command(description="Тебе интересно что делаю я?")
async def cho_delaesh(ctx):
    await ctx.send("Я жду пока `Elezthem#7007` до кодит меня) а ты?")

@bot.command()
async def communicate(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Поняла, принятного общения с друзьями")

@bot.slash_command(description="Аки интересно что ты делаешь)")
async def communicte(ctx):
    await ctx.send("Поняла) Приятного общение тебе с друзьями!")

@bot.command()
async def bye(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Поки, если хочешь еще пообщаться то пиши, я рада с всеми общаться)")

@bot.slash_command(description="Попрощаться со мной(")
async def bye(ctx):
    await ctx.send("Пока, мне было приятно с тобой провести время! Приходи еще))")

@bot.command()
async def xz(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||")

@bot.slash_command(description="ХЗ :D")
async def xz(ctx):
    await ctx.send("||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||  ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||")

@bot.command()
async def helpserver(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Саппорт сервер бота - https://discord.gg/xqS4ApXvey | Ссылка на сервер разработчика - https://discord.gg/4JXqupbuPq (можешь зайти по желанию)")

@bot.slash_command(description="Саппорт сервер")
async def helpserver(ctx):
    await ctx.send("Саппорт сервер бота - https://discord.gg/xqS4ApXvey | Ссылка на сервер разработчика - https://discord.gg/4JXqupbuPq (можешь зайти по желанию)")

@bot.command()
async def shapi(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Шни Шна Шнапи | Шнапи Шнапи Шнап | Шни Шна Шнапи | Шнапи Шнапи Шнап.")

@bot.slash_command(description="Шни шна шапи")
async def shapi(ctx):
    await ctx.send("Шни Шна Шнапи | Шнапи Шнапи Шнап | Шни Шна Шнапи | Шнапи Шнапи Шнап.")

@bot.command()
async def kira(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"Процент того что {ctx.author.mention} станет Кирой равен 38% или 28%.")

@bot.slash_command(description="Какой у тебя шанс стать Кирой?")
async def kira(ctx):
    await ctx.send(f"Процент того что **ТЫ** станешь Кирой равен 48% или 78%.")

@bot.command()
async def prefix(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"Мой префикс `.` (Сделал запрос {ctx.author.mention})")

@bot.slash_command(description="Мой префикс")
async def prefix(ctx):
    await ctx.send("Мой префикс `.`")

@bot.command()
async def bob (ctx, *, text=None):
    bob = ["https://i.gifer.com/origin/00/005af152556a7ab6b55dc05b165a3da9.gif", "https://i.gifer.com/5Nzx.gif", "https://media.tenor.com/bjkVrV9RqqUAAAAC/deal-its-a-deal.gif", "https://media.tenor.com/r5bF5LVD5D4AAAAC/study-cramming.gif", "https://i.pinimg.com/originals/94/b0/01/94b001c3aadb873ff3aacc89079c2f02.gif", "https://i.pinimg.com/originals/9d/a6/86/9da686b3a376fdfa7fa6a7200e6a9980.gif", "https://vgif.ru/gifs/145/vgif-ru-19259.gif", "https://i.gifer.com/5SOd.gif", "https://i.gifer.com/origin/27/2704b6bfdf35585c74423a73fa7d01ac_w200.gif", "https://i.pinimg.com/originals/f6/46/3a/f6463a68f1bb97e2ddaade930cc4207a.gif", "https://liubavyshka.ru/_ph/176/2/270222183.gif", "https://vgif.ru/gifs/142/vgif-ru-17638.gif", "https://media.tenor.com/n7QEggliJPQAAAAC/sponge-bob-bla-bla-bla.gif", "https://thumbs.gfycat.com/ElderlyHilariousGuanaco-max-1mb.gif", "https://media.tenor.com/FI7Pj4jcpBoAAAAC/sponge-bob-sponge-bob-square-pants.gif", "https://i.gifer.com/4Sbu.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с spongebob**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(bob)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="bob", description="Рандомная картинка с ( Спанч боб )")
async def bob (ctx, *, text=None):
    bob = ["https://i.gifer.com/origin/00/005af152556a7ab6b55dc05b165a3da9.gif", "https://i.gifer.com/5Nzx.gif", "https://media.tenor.com/bjkVrV9RqqUAAAAC/deal-its-a-deal.gif", "https://media.tenor.com/r5bF5LVD5D4AAAAC/study-cramming.gif", "https://i.pinimg.com/originals/94/b0/01/94b001c3aadb873ff3aacc89079c2f02.gif", "https://i.pinimg.com/originals/9d/a6/86/9da686b3a376fdfa7fa6a7200e6a9980.gif", "https://vgif.ru/gifs/145/vgif-ru-19259.gif", "https://i.gifer.com/5SOd.gif", "https://i.gifer.com/origin/27/2704b6bfdf35585c74423a73fa7d01ac_w200.gif", "https://i.pinimg.com/originals/f6/46/3a/f6463a68f1bb97e2ddaade930cc4207a.gif", "https://liubavyshka.ru/_ph/176/2/270222183.gif", "https://vgif.ru/gifs/142/vgif-ru-17638.gif", "https://media.tenor.com/n7QEggliJPQAAAAC/sponge-bob-bla-bla-bla.gif", "https://thumbs.gfycat.com/ElderlyHilariousGuanaco-max-1mb.gif", "https://media.tenor.com/FI7Pj4jcpBoAAAAC/sponge-bob-sponge-bob-square-pants.gif", "https://i.gifer.com/4Sbu.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с spongebob**')
        emb1.set_image(url=f'{random.choice(bob)}')
        await ctx.send(embed=emb1)

@bot.command()
async def tekashi69 (ctx, *, text=None):
    tekashi69 = ["https://media.tenor.com/EMJa1tdItrcAAAAC/tekashi-tekashi69.gif", "https://media.tenor.com/OKS6fzjDRksAAAAd/tekashi-6ix9ine.gif", "https://media2.giphy.com/media/75fMkn3s4mZbK4AeGI/giphy.gif", "https://media.tenor.com/EZ7WiW8EhSIAAAAM/gooba-daniel-hernandez.gif", "https://i.pinimg.com/originals/3e/14/ac/3e14ace2419a4983b3438a4506b82f41.gif", "https://thumbs.gfycat.com/AgonizingSoulfulHake-max-1mb.gif", "https://i.pinimg.com/originals/18/95/34/189534e6352b1f93b99dc1cd082cbea7.gif", "https://thumbs.gfycat.com/AlarmedGorgeousEkaltadeta-size_restricted.gif", "https://media.tenor.com/CNGTw4yQi7AAAAAC/6ix9ine-69.gif", "https://media.tenor.com/_He10QErFtAAAAAC/tekashi-dog.gif", "https://media4.giphy.com/media/3kAJJNc8aKDZ2P8UGR/giphy.gif", "https://thumbs.gfycat.com/CluelessQuarterlyLiger-max-1mb.gif", "https://media.tenor.com/YLWfo2vJofIAAAAC/6ix9ine-69.gif", "https://hollywoodunlocked.com/wp-content/uploads/2020/04/0401DBC5-7109-4F11-B606-C34D6D962F60.gif", "https://hollywoodunlocked.com/wp-content/uploads/2020/05/Tekashi-6ix9ine-GIF.gif", "https://thumbs.gfycat.com/JovialWillingCicada-size_restricted.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Tekashi 6ix9ine**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(tekashi69)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="tekashi69", description="Рандомная картинка с ( СиксНайн )")
async def tekashi69 (ctx, *, text=None):
    tekashi69 = ["https://media.tenor.com/EMJa1tdItrcAAAAC/tekashi-tekashi69.gif", "https://media.tenor.com/OKS6fzjDRksAAAAd/tekashi-6ix9ine.gif", "https://media2.giphy.com/media/75fMkn3s4mZbK4AeGI/giphy.gif", "https://media.tenor.com/EZ7WiW8EhSIAAAAM/gooba-daniel-hernandez.gif", "https://i.pinimg.com/originals/3e/14/ac/3e14ace2419a4983b3438a4506b82f41.gif", "https://thumbs.gfycat.com/AgonizingSoulfulHake-max-1mb.gif", "https://i.pinimg.com/originals/18/95/34/189534e6352b1f93b99dc1cd082cbea7.gif", "https://thumbs.gfycat.com/AlarmedGorgeousEkaltadeta-size_restricted.gif", "https://media.tenor.com/CNGTw4yQi7AAAAAC/6ix9ine-69.gif", "https://media.tenor.com/_He10QErFtAAAAAC/tekashi-dog.gif", "https://media4.giphy.com/media/3kAJJNc8aKDZ2P8UGR/giphy.gif", "https://thumbs.gfycat.com/CluelessQuarterlyLiger-max-1mb.gif", "https://media.tenor.com/YLWfo2vJofIAAAAC/6ix9ine-69.gif", "https://hollywoodunlocked.com/wp-content/uploads/2020/04/0401DBC5-7109-4F11-B606-C34D6D962F60.gif", "https://hollywoodunlocked.com/wp-content/uploads/2020/05/Tekashi-6ix9ine-GIF.gif", "https://thumbs.gfycat.com/JovialWillingCicada-size_restricted.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Tekashi 6ix9ine**')
        emb1.set_image(url=f'{random.choice(tekashi69)}')
        await ctx.send(embed=emb1)

@bot.command()
async def morgen (ctx, *, text=None):
    morgen = ["https://thumbs.gfycat.com/WigglyImaginativeAnkolewatusi-size_restricted.gif", "https://thumbs.gfycat.com/AromaticIdealAzurevase-max-1mb.gif", "https://64.media.tumblr.com/82a8368810ed62e73acfbc040d0d7507/a316adfaa07d896e-a5/s500x750/55ab946927c87ad3919422c3313d197cf5649147.gif", "https://thumbs.gfycat.com/InsignificantEssentialFennecfox-max-1mb.gif", "https://64.media.tumblr.com/461c588fd337ad76ce9d30f3f76f7a71/62e722e54822a78b-34/s500x750/3112e4422f9ed79cc9fdd77b341b23f8edf83aa0.gif", "https://media.tenor.com/NBEre5J2z-4AAAAC/morgenshtern.gif", "https://media.tenor.com/tCjmWwxU_UQAAAAM/morgenshtern.gif", "https://i.pinimg.com/originals/5e/71/ba/5e71bad6d5a8a26201ff5446fd81518b.gif", "https://steamuserimages-a.akamaihd.net/ugc/956342334657192586/F185F8A28C781E1BF570692515D1A63D2AADB80C/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "https://thumbs.gfycat.com/SlimyBonyGrouper-max-1mb.gif", "https://media.tenor.com/OZNVPueikzMAAAAM/morgenshtern-hummer.gif", "https://i.makeagif.com/media/6-25-2021/VZCw9M.gif", "https://media.tenor.com/Muv9wWpCmT4AAAAd/morgenstern-%D0%BC%D0%BE%D1%80%D0%B3%D0%B5%D0%BD%D1%88%D1%82%D0%B5%D1%80%D0%BD.gif", "https://j.gifs.com/XLnZ5m.gif", "https://i.makeagif.com/media/6-18-2021/8NiLk3.gif", "https://i.makeagif.com/media/7-10-2021/iI2Tj8.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Morgenshtern**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(morgen)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="morgen", description="Рандомная картинка с ( Morgenshtern )")
async def morgen (ctx, *, text=None):
    morgen = ["https://thumbs.gfycat.com/WigglyImaginativeAnkolewatusi-size_restricted.gif", "https://thumbs.gfycat.com/AromaticIdealAzurevase-max-1mb.gif", "https://64.media.tumblr.com/82a8368810ed62e73acfbc040d0d7507/a316adfaa07d896e-a5/s500x750/55ab946927c87ad3919422c3313d197cf5649147.gif", "https://thumbs.gfycat.com/InsignificantEssentialFennecfox-max-1mb.gif", "https://64.media.tumblr.com/461c588fd337ad76ce9d30f3f76f7a71/62e722e54822a78b-34/s500x750/3112e4422f9ed79cc9fdd77b341b23f8edf83aa0.gif", "https://media.tenor.com/NBEre5J2z-4AAAAC/morgenshtern.gif", "https://media.tenor.com/tCjmWwxU_UQAAAAM/morgenshtern.gif", "https://i.pinimg.com/originals/5e/71/ba/5e71bad6d5a8a26201ff5446fd81518b.gif", "https://steamuserimages-a.akamaihd.net/ugc/956342334657192586/F185F8A28C781E1BF570692515D1A63D2AADB80C/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "https://thumbs.gfycat.com/SlimyBonyGrouper-max-1mb.gif", "https://media.tenor.com/OZNVPueikzMAAAAM/morgenshtern-hummer.gif", "https://i.makeagif.com/media/6-25-2021/VZCw9M.gif", "https://media.tenor.com/Muv9wWpCmT4AAAAd/morgenstern-%D0%BC%D0%BE%D1%80%D0%B3%D0%B5%D0%BD%D1%88%D1%82%D0%B5%D1%80%D0%BD.gif", "https://j.gifs.com/XLnZ5m.gif", "https://i.makeagif.com/media/6-18-2021/8NiLk3.gif", "https://i.makeagif.com/media/7-10-2021/iI2Tj8.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Morgenshtern**')
        emb1.set_image(url=f'{random.choice(morgen)}')
        await ctx.send(embed=emb1)

@bot.command()
async def bbt (ctx, *, text=None):
    bbt = ["https://media.tenor.com/z8hVUlH5TZ4AAAAC/big-baby-tape-kizaru.gif", "https://media.tenor.com/SSU5Gs1jktEAAAAC/big-baby-tape-newtape.gif", "https://thumbs.gfycat.com/SlipperySlimAnt-max-1mb.gif", "https://media.tenor.com/DEVCr42ZPEcAAAAC/big-baby-tape-killcar.gif", "https://media.tenor.com/3BbSiHLZtWYAAAAC/big-baby-tape.gif", "https://thumbs.gfycat.com/AdorableSinfulAfricanparadiseflycatcher-size_restricted.gif", "https://media.tenor.com/EzjHVZi4UMUAAAAM/big-baby-tape-kari.gif", "https://thumbs.gfycat.com/JealousFortunateGypsymoth-size_restricted.gif", "https://media.tenor.com/AWiqi2IpVBIAAAAM/bbt-baby-tape-dance.gif", "https://media.tenor.com/1A_G4456T40AAAAM/bang-woah.gif", "https://media.tenor.com/s12RluIKbpEAAAAM/bigbabytape-fastfoodmusic.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Big Baby Tape**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(bbt)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="bbt", description="Рандомная картинка с ( Big Baby Tape )")
async def bbt (ctx, *, text=None):
    bbt = ["https://media.tenor.com/z8hVUlH5TZ4AAAAC/big-baby-tape-kizaru.gif", "https://media.tenor.com/SSU5Gs1jktEAAAAC/big-baby-tape-newtape.gif", "https://thumbs.gfycat.com/SlipperySlimAnt-max-1mb.gif", "https://media.tenor.com/DEVCr42ZPEcAAAAC/big-baby-tape-killcar.gif", "https://media.tenor.com/3BbSiHLZtWYAAAAC/big-baby-tape.gif", "https://thumbs.gfycat.com/AdorableSinfulAfricanparadiseflycatcher-size_restricted.gif", "https://media.tenor.com/EzjHVZi4UMUAAAAM/big-baby-tape-kari.gif", "https://thumbs.gfycat.com/JealousFortunateGypsymoth-size_restricted.gif", "https://media.tenor.com/AWiqi2IpVBIAAAAM/bbt-baby-tape-dance.gif", "https://media.tenor.com/1A_G4456T40AAAAM/bang-woah.gif", "https://media.tenor.com/s12RluIKbpEAAAAM/bigbabytape-fastfoodmusic.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Big Baby Tape**')
        emb1.set_image(url=f'{random.choice(bbt)}')
        await ctx.send(embed=emb1)

@bot.command()
async def kizaru (ctx, *, text=None):
    kizaru = ["https://media.tenor.com/YehZyR6x-RsAAAAd/kizaru-%D0%BA%D0%B8%D0%B7%D0%B0%D1%80%D1%83.gif", "https://thumbs.gfycat.com/CoolSpottedDiscus-max-1mb.gif", "https://media.tenor.com/tLeDLGbbJOEAAAAM/kizaru-bandana.gif", "https://media.tenor.com/ZkXAla4BbDYAAAAM/kizaru-%D1%85%D0%BB%D0%BE%D0%BF%D0%BD%D1%83%D0%BB%D0%B8.gif", "https://media.tenor.com/0OSdiMzehCQAAAAM/kizaru-pharmacist.gif", "https://media.tenor.com/Y4Gm8BCuVTkAAAAM/kizaru-kizaru-music.gif", "https://media.tenor.com/XdwgLg3EXEgAAAAM/%D0%BA%D0%B8%D0%B7%D0%B0%D1%80%D1%83-%D0%BA%D0%B8%D0%B7%D1%8F%D0%BA%D0%B0.gif", "https://i.makeagif.com/media/12-18-2016/fVGyO3.gif", "https://thumbs.gfycat.com/DefensivePlainArgali-max-1mb.gif", "https://steamuserimages-a.akamaihd.net/ugc/869619208163498490/DFD712A190E9854F869D332B0F899EC824584DE9/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "https://thumbs.gfycat.com/BareAromaticBubblefish-max-1mb.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с kizaru**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(kizaru)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="kizaru", description="Рандомная картинка с ( kizaru )")
async def kizaru (ctx, *, text=None):
    kizaru = ["https://media.tenor.com/YehZyR6x-RsAAAAd/kizaru-%D0%BA%D0%B8%D0%B7%D0%B0%D1%80%D1%83.gif", "https://thumbs.gfycat.com/CoolSpottedDiscus-max-1mb.gif", "https://media.tenor.com/tLeDLGbbJOEAAAAM/kizaru-bandana.gif", "https://media.tenor.com/ZkXAla4BbDYAAAAM/kizaru-%D1%85%D0%BB%D0%BE%D0%BF%D0%BD%D1%83%D0%BB%D0%B8.gif", "https://media.tenor.com/0OSdiMzehCQAAAAM/kizaru-pharmacist.gif", "https://media.tenor.com/Y4Gm8BCuVTkAAAAM/kizaru-kizaru-music.gif", "https://media.tenor.com/XdwgLg3EXEgAAAAM/%D0%BA%D0%B8%D0%B7%D0%B0%D1%80%D1%83-%D0%BA%D0%B8%D0%B7%D1%8F%D0%BA%D0%B0.gif", "https://i.makeagif.com/media/12-18-2016/fVGyO3.gif", "https://thumbs.gfycat.com/DefensivePlainArgali-max-1mb.gif", "https://steamuserimages-a.akamaihd.net/ugc/869619208163498490/DFD712A190E9854F869D332B0F899EC824584DE9/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "https://thumbs.gfycat.com/BareAromaticBubblefish-max-1mb.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с kizaru**')
        emb1.set_image(url=f'{random.choice(kizaru)}')
        await ctx.send(embed=emb1)

@bot.command()
async def lilpump (ctx, *, text=None):
    lilpump = ["https://media.tenor.com/38vPm5bkb5EAAAAC/lil-pump-rapping.gif", "https://media.tenor.com/vQ5NZFjInl8AAAAC/lil-pump.gif", "https://media4.giphy.com/media/dYZB8uP3WHqeQ57Xp6/giphy.gif", "https://thumbs.gfycat.com/BoilingGrimyHammerkop-max-1mb.gif", "https://i.pinimg.com/originals/18/e0/0a/18e00a099350592d54e19cc0463b717e.gif", "https://thumbs.gfycat.com/GlamorousOldfashionedAustrianpinscher-size_restricted.gif", "https://media.tenor.com/75T5vqJlJq4AAAAC/lil-pump-smoke.gif", "https://i.pinimg.com/originals/7f/cc/64/7fcc643c0476344b9f8cd7786616ea91.gif", "https://media2.giphy.com/media/ORhoofTYKqRvdUAFV3/giphy.gif", "https://i.makeagif.com/media/12-14-2017/F_O-TI.gif", "https://media.tenor.com/pFdyEGYM2t4AAAAC/lil-pump-hiphop.gif", "https://thumbs.gfycat.com/BaggyEvergreenHeifer-max-1mb.gif", "https://i.makeagif.com/media/7-21-2017/XYXySS.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Lil Pump**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(lilpump)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="lilpump", description="Рандомная картинка с ( lilpump )")
async def lilpump (ctx, *, text=None):
    lilpump = ["https://media.tenor.com/38vPm5bkb5EAAAAC/lil-pump-rapping.gif", "https://media.tenor.com/vQ5NZFjInl8AAAAC/lil-pump.gif", "https://media4.giphy.com/media/dYZB8uP3WHqeQ57Xp6/giphy.gif", "https://thumbs.gfycat.com/BoilingGrimyHammerkop-max-1mb.gif", "https://i.pinimg.com/originals/18/e0/0a/18e00a099350592d54e19cc0463b717e.gif", "https://thumbs.gfycat.com/GlamorousOldfashionedAustrianpinscher-size_restricted.gif", "https://media.tenor.com/75T5vqJlJq4AAAAC/lil-pump-smoke.gif", "https://i.pinimg.com/originals/7f/cc/64/7fcc643c0476344b9f8cd7786616ea91.gif", "https://media2.giphy.com/media/ORhoofTYKqRvdUAFV3/giphy.gif", "https://i.makeagif.com/media/12-14-2017/F_O-TI.gif", "https://media.tenor.com/pFdyEGYM2t4AAAAC/lil-pump-hiphop.gif", "https://thumbs.gfycat.com/BaggyEvergreenHeifer-max-1mb.gif", "https://i.makeagif.com/media/7-21-2017/XYXySS.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с lilpump**')
        emb1.set_image(url=f'{random.choice(lilpump)}')
        await ctx.send(embed=emb1)

@bot.command()
async def lilpeep (ctx, *, text=None):
    lilpeep = ["https://media.tenor.com/Xs1iQgafTUQAAAAM/lil-peep-rapper.gif", "https://media.tenor.com/F5X43uzEpBAAAAAM/lil-peep.gif", "https://media.tenor.com/TVDVBIifsdsAAAAM/lil-peep-rip-gus.gif", "https://i.pinimg.com/originals/f8/a0/86/f8a08621f3a64394f2b8e22de62ed376.gif", "https://i.gifer.com/SqSq.gif", "https://i.pinimg.com/originals/0c/db/29/0cdb29cd3fb440a38bb15b7592b6e019.gif", "https://media.tenor.com/052n0-rKKhwAAAAM/lil-peep.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2bbac9ac-8687-40e8-8ff3-dc6bbfcfa200/dc0lk3b-4a851212-9fe4-4834-91e2-5116f23223d1.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJiYmFjOWFjLTg2ODctNDBlOC04ZmYzLWRjNmJiZmNmYTIwMFwvZGMwbGszYi00YTg1MTIxMi05ZmU0LTQ4MzQtOTFlMi01MTE2ZjIzMjIzZDEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.l5C6QWaqzTaHRKNX9Zbmr1-iBMqjj4NIcpU0oVFjvuM", "https://thumbs.gfycat.com/DimpledFemaleAntarcticfurseal-max-1mb.gif", "https://www.icegif.com/wp-content/uploads/2022/06/icegif-106.gif", "https://i.pinimg.com/originals/96/dc/c6/96dcc63a520038733b42ffc13ac1e2f8.gif", "https://i.gifer.com/SqSn.gif", "https://media.tenor.com/fewHfVf_vbcAAAAM/lil-peep.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Lil Peep**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(lilpeep)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="lilpeep", description="Рандомная картинка с ( lilpeep )")
async def lilpeep (ctx, *, text=None):
    lilpeep = ["https://media.tenor.com/Xs1iQgafTUQAAAAM/lil-peep-rapper.gif", "https://media.tenor.com/F5X43uzEpBAAAAAM/lil-peep.gif", "https://media.tenor.com/TVDVBIifsdsAAAAM/lil-peep-rip-gus.gif", "https://i.pinimg.com/originals/f8/a0/86/f8a08621f3a64394f2b8e22de62ed376.gif", "https://i.gifer.com/SqSq.gif", "https://i.pinimg.com/originals/0c/db/29/0cdb29cd3fb440a38bb15b7592b6e019.gif", "https://media.tenor.com/052n0-rKKhwAAAAM/lil-peep.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2bbac9ac-8687-40e8-8ff3-dc6bbfcfa200/dc0lk3b-4a851212-9fe4-4834-91e2-5116f23223d1.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJiYmFjOWFjLTg2ODctNDBlOC04ZmYzLWRjNmJiZmNmYTIwMFwvZGMwbGszYi00YTg1MTIxMi05ZmU0LTQ4MzQtOTFlMi01MTE2ZjIzMjIzZDEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.l5C6QWaqzTaHRKNX9Zbmr1-iBMqjj4NIcpU0oVFjvuM", "https://thumbs.gfycat.com/DimpledFemaleAntarcticfurseal-max-1mb.gif", "https://www.icegif.com/wp-content/uploads/2022/06/icegif-106.gif", "https://i.pinimg.com/originals/96/dc/c6/96dcc63a520038733b42ffc13ac1e2f8.gif", "https://i.gifer.com/SqSn.gif", "https://media.tenor.com/fewHfVf_vbcAAAAM/lil-peep.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с lilpeep**')
        emb1.set_image(url=f'{random.choice(lilpeep)}')
        await ctx.send(embed=emb1)

@bot.command()
async def falls (ctx, *, text=None):
    falls = ["https://i.gifer.com/X2F.gif", "https://i.gifer.com/X1z.gif", "https://c.tenor.com/EYpMK3v_VG8AAAAM/gravity-falls-mabel-pines.gif", "https://i.pinimg.com/originals/fc/e3/5d/fce35dd265b90ced476f6c91e3bd54b1.gif", "https://i.pinimg.com/originals/a3/41/09/a34109ae6b4d18be01853c3a95ed1fae.gif", "https://media.tenor.com/f7aHCDTyWxMAAAAC/pig-piggy.gif", "https://static.wikia.nocookie.net/gravityfalls/images/e/e2/Smile_Dip.gif/revision/latest/scale-to-width-down/640?cb=20160312062334&path-prefix=ru", "https://i.pinimg.com/originals/4a/59/d5/4a59d5db2a453333235daebf1dc9b6b7.gif", "https://i.gifer.com/2vcV.gif", "https://cs4.pikabu.ru/post_img/2014/10/09/12/1412882228_1080516716.gif", "https://media.tenor.com/vnPapVJ8AkcAAAAC/mabelpines-dipper.gif", "https://i.gifer.com/1GW7.gif", "https://www.youloveit.ru/uploads/posts/2017-07/1501068194_youloveit_ru_svitera_meibl_gifki01.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Graffiti Falls**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(falls)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="falls", description="Рандомная картинка с ( falls )")
async def falls (ctx, *, text=None):
    falls = ["https://i.gifer.com/X2F.gif", "https://i.gifer.com/X1z.gif", "https://c.tenor.com/EYpMK3v_VG8AAAAM/gravity-falls-mabel-pines.gif", "https://i.pinimg.com/originals/fc/e3/5d/fce35dd265b90ced476f6c91e3bd54b1.gif", "https://i.pinimg.com/originals/a3/41/09/a34109ae6b4d18be01853c3a95ed1fae.gif", "https://media.tenor.com/f7aHCDTyWxMAAAAC/pig-piggy.gif", "https://static.wikia.nocookie.net/gravityfalls/images/e/e2/Smile_Dip.gif/revision/latest/scale-to-width-down/640?cb=20160312062334&path-prefix=ru", "https://i.pinimg.com/originals/4a/59/d5/4a59d5db2a453333235daebf1dc9b6b7.gif", "https://i.gifer.com/2vcV.gif", "https://cs4.pikabu.ru/post_img/2014/10/09/12/1412882228_1080516716.gif", "https://media.tenor.com/vnPapVJ8AkcAAAAC/mabelpines-dipper.gif", "https://i.gifer.com/1GW7.gif", "https://www.youloveit.ru/uploads/posts/2017-07/1501068194_youloveit_ru_svitera_meibl_gifki01.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с falls**')
        emb1.set_image(url=f'{random.choice(falls)}')
        await ctx.send(embed=emb1)

@bot.command()
async def squirrel (ctx, *, text=None):
    squirrel = ["https://media.tenor.com/FuwRi3YgdaQAAAAC/lyubov-love.gif", "https://i.gifer.com/RDMM.gif", "https://i.gifer.com/origin/8f/8f917283df63e6a5f793a94e64588d48.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz29e.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz289.gif", "https://i.gifer.com/RWkD.gif", "https://phoneky.co.uk/thumbs/screensavers/down/movies/iceage3_hv319dkd.gif", "https://cs5.pikabu.ru/post_img/2014/07/20/10/1405872591_1277524344.gif", "https://media.tenor.com/_x8sFvn1QwMAAAAd/%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4.gif", "https://www.yapfiles.ru/files/1142046/lednikovyjperiod21.gif", "https://media.rbcdn.ru/media/news/rb491889720071107124423.gif", "https://img-s3.onedio.com/id-5cd43edb53efbac94b993804/rev-0/w-635/listing/f-jpg-gif-webp-webm-mp4/s-69fe10d0301f1ceb902024d2a1d718bc1f9ac66e.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz283.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Белкой**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(squirrel)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="squirrel", description="Рандомная картинка с ( squirrel )")
async def squirrel (ctx, *, text=None):
    squirrel = ["https://media.tenor.com/FuwRi3YgdaQAAAAC/lyubov-love.gif", "https://i.gifer.com/RDMM.gif", "https://i.gifer.com/origin/8f/8f917283df63e6a5f793a94e64588d48.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz29e.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz289.gif", "https://i.gifer.com/RWkD.gif", "https://phoneky.co.uk/thumbs/screensavers/down/movies/iceage3_hv319dkd.gif", "https://cs5.pikabu.ru/post_img/2014/07/20/10/1405872591_1277524344.gif", "https://media.tenor.com/_x8sFvn1QwMAAAAd/%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4.gif", "https://www.yapfiles.ru/files/1142046/lednikovyjperiod21.gif", "https://media.rbcdn.ru/media/news/rb491889720071107124423.gif", "https://img-s3.onedio.com/id-5cd43edb53efbac94b993804/rev-0/w-635/listing/f-jpg-gif-webp-webm-mp4/s-69fe10d0301f1ceb902024d2a1d718bc1f9ac66e.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz283.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с squirrel**')
        emb1.set_image(url=f'{random.choice(squirrel)}')
        await ctx.send(embed=emb1)

@bot.command()
async def tom (ctx, *, text=None):
    tom = ["https://media.tenor.com/JqxVqlU-M0IAAAAC/%D1%82%D0%BE%D0%BC-%D0%B8.gif", "https://thumbs.gfycat.com/AdvancedOfficialGermanwirehairedpointer-size_restricted.gif", "https://media.tenor.com/dHFl6B38ZMcAAAAC/lullaby-tom-and-jerry.gif", "https://i.gifer.com/22z.gif", "https://media3.giphy.com/media/6BZaFXBVPBtok/giphy.gif", "https://thumbs.gfycat.com/BowedRewardingAsianlion-size_restricted.gif", "https://i.pinimg.com/originals/00/0a/02/000a022bf18954b1104b7ac9c863d91e.gif", "https://i.gifer.com/162H.gif", "https://www.gifcen.com/wp-content/uploads/2021/09/tom-and-jerry-gif-13.gif", "https://media.tenor.com/m4Z3TEfV67QAAAAC/%D0%BE%D0%B1%D0%BD%D0%B8%D0%BC%D0%B0%D1%8E-%D1%82%D0%BE%D0%BC.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz26f.gif", "https://i.pinimg.com/originals/35/e3/fe/35e3fe6e906b0a408dc7476adfbdbab4.gif", "https://media0.giphy.com/media/QzMC1llfXkNbX5wsTC/200w.gif?cid=6c09b952cy0y2p1y4ojysdvgxhspbgf5nvb49knx0q7evc0d&rid=200w.gif&ct=g"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Tom and Jerry**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(tom)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="tom", description="Рандомная картинка с ( tom )")
async def tom (ctx, *, text=None):
    tom = ["https://media.tenor.com/JqxVqlU-M0IAAAAC/%D1%82%D0%BE%D0%BC-%D0%B8.gif", "https://thumbs.gfycat.com/AdvancedOfficialGermanwirehairedpointer-size_restricted.gif", "https://media.tenor.com/dHFl6B38ZMcAAAAC/lullaby-tom-and-jerry.gif", "https://i.gifer.com/22z.gif", "https://media3.giphy.com/media/6BZaFXBVPBtok/giphy.gif", "https://thumbs.gfycat.com/BowedRewardingAsianlion-size_restricted.gif", "https://i.pinimg.com/originals/00/0a/02/000a022bf18954b1104b7ac9c863d91e.gif", "https://i.gifer.com/162H.gif", "https://www.gifcen.com/wp-content/uploads/2021/09/tom-and-jerry-gif-13.gif", "https://media.tenor.com/m4Z3TEfV67QAAAAC/%D0%BE%D0%B1%D0%BD%D0%B8%D0%BC%D0%B0%D1%8E-%D1%82%D0%BE%D0%BC.gif", "https://otkritkis.com/wp-content/uploads/2022/07/gz26f.gif", "https://i.pinimg.com/originals/35/e3/fe/35e3fe6e906b0a408dc7476adfbdbab4.gif", "https://media0.giphy.com/media/QzMC1llfXkNbX5wsTC/200w.gif?cid=6c09b952cy0y2p1y4ojysdvgxhspbgf5nvb49knx0q7evc0d&rid=200w.gif&ct=g"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с tom**')
        emb1.set_image(url=f'{random.choice(tom)}')
        await ctx.send(embed=emb1)

@bot.command()
async def skala (ctx, *, text=None):
    skala = ["https://media.tenor.com/M0YyxTY9gB0AAAAC/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/qwR44XG-f5kAAAAd/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/25FN1Vr-YlEAAAAd/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/wSmicMRFetAAAAAM/good-%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://i.gifer.com/origin/e1/e1a0362291858704234da89172062e65.gif", "https://media.tenor.com/yI2nog_b9y4AAAAd/skala-ne-ponimat-%D1%81%D0%BA%D0%B0%D0%BB%D0%B0%D0%BD%D0%B5%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%B5%D1%82.gif", "https://media.tenor.com/4fn3GX0oa34AAAAd/rock-sit-rock.gif", "https://i.gifer.com/THGu.gif", "https://i.gifer.com/origin/6a/6a67d44d843c6ffbc5c5b459611ae98c_w200.gif", "https://media.tenor.com/monpyTLawL4AAAAC/dwayne-johnson-the-rock.gif", "https://media.tenor.com/8__cICPc1SQAAAAC/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0-%D1%8F%D0%BF%D0%BE%D1%81%D1%80%D0%B0%D0%BB.gif", "https://media.tenor.com/bI2mRWCV6XgAAAAd/skala.gif", "https://media.tenor.com/x2ZGRDye_okAAAAC/dwayne-johnson-the-rock.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Скалой Джонсоном**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(skala)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="skala", description="Рандомная картинка с ( skala )")
async def skala (ctx, *, text=None):
    skala = ["https://media.tenor.com/M0YyxTY9gB0AAAAC/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/qwR44XG-f5kAAAAd/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/25FN1Vr-YlEAAAAd/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://media.tenor.com/wSmicMRFetAAAAAM/good-%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif", "https://i.gifer.com/origin/e1/e1a0362291858704234da89172062e65.gif", "https://media.tenor.com/yI2nog_b9y4AAAAd/skala-ne-ponimat-%D1%81%D0%BA%D0%B0%D0%BB%D0%B0%D0%BD%D0%B5%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%B5%D1%82.gif", "https://media.tenor.com/4fn3GX0oa34AAAAd/rock-sit-rock.gif", "https://i.gifer.com/THGu.gif", "https://i.gifer.com/origin/6a/6a67d44d843c6ffbc5c5b459611ae98c_w200.gif", "https://media.tenor.com/monpyTLawL4AAAAC/dwayne-johnson-the-rock.gif", "https://media.tenor.com/8__cICPc1SQAAAAC/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0-%D1%8F%D0%BF%D0%BE%D1%81%D1%80%D0%B0%D0%BB.gif", "https://media.tenor.com/bI2mRWCV6XgAAAAd/skala.gif", "https://media.tenor.com/x2ZGRDye_okAAAAC/dwayne-johnson-the-rock.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с skala**')
        emb1.set_image(url=f'{random.choice(skala)}')
        await ctx.send(embed=emb1)

@bot.command()
async def tsoy (ctx, *, text=None):
    tsoy = ["https://media.tenor.com/uwJ2n0DimeoAAAAC/viktor-tsoy-tsoy.gif", "https://media.tenor.com/Wx59o-hm6lwAAAAC/tsoy-kino.gif", "https://media.tenor.com/KfVmY4OMpV8AAAAM/kino-viktor-tsoi.gif", "https://thumbs.gfycat.com/SentimentalQualifiedArkshell-max-1mb.gif", "https://cs4.pikabu.ru/post_img/2015/02/23/0/1424638897_729332529.gif", "https://thumbs.gfycat.com/LittleReasonableGopher-max-1mb.gif", "https://media.tenor.com/rZ-EzkGwTKMAAAAC/tsoy-leave-me-alone.gif", "https://s00.yaplakal.com/pics/pics_original/8/0/8/14522808.gif", "https://media.tenor.com/TYCmOZVjecYAAAAM/viktor-tsoi-%D0%B2%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D1%86%D0%BE%D0%B9.gif", "https://64.media.tumblr.com/0cbd7bf642d1096893f698921be14fcc/d5cb40f08048b6d8-07/s540x810/4456031cba3d5ebeca890d8b341a690b5ddd4f72.gif", "https://media.tenor.com/mwYwWSSjf4kAAAAM/tsoy-see-you.gif", "https://media.tenor.com/QWJassnTGRYAAAAd/%D1%86%D0%BE%D0%B9-snow.gif", "https://i.makeagif.com/media/8-07-2015/yHgDlV.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Цой**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(tsoy)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="tsoy", description="Рандомная картинка с ( tsoy )")
async def tsoy (ctx, *, text=None):
    tsoy = ["https://media.tenor.com/uwJ2n0DimeoAAAAC/viktor-tsoy-tsoy.gif", "https://media.tenor.com/Wx59o-hm6lwAAAAC/tsoy-kino.gif", "https://media.tenor.com/KfVmY4OMpV8AAAAM/kino-viktor-tsoi.gif", "https://thumbs.gfycat.com/SentimentalQualifiedArkshell-max-1mb.gif", "https://cs4.pikabu.ru/post_img/2015/02/23/0/1424638897_729332529.gif", "https://thumbs.gfycat.com/LittleReasonableGopher-max-1mb.gif", "https://media.tenor.com/rZ-EzkGwTKMAAAAC/tsoy-leave-me-alone.gif", "https://s00.yaplakal.com/pics/pics_original/8/0/8/14522808.gif", "https://media.tenor.com/TYCmOZVjecYAAAAM/viktor-tsoi-%D0%B2%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D1%86%D0%BE%D0%B9.gif", "https://64.media.tumblr.com/0cbd7bf642d1096893f698921be14fcc/d5cb40f08048b6d8-07/s540x810/4456031cba3d5ebeca890d8b341a690b5ddd4f72.gif", "https://media.tenor.com/mwYwWSSjf4kAAAAM/tsoy-see-you.gif", "https://media.tenor.com/QWJassnTGRYAAAAd/%D1%86%D0%BE%D0%B9-snow.gif", "https://i.makeagif.com/media/8-07-2015/yHgDlV.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с tsoy**')
        emb1.set_image(url=f'{random.choice(tsoy)}')
        await ctx.send(embed=emb1)

@bot.command()
async def fox (ctx, *, text=None):
    fox = ["https://media.tenor.com/pdiR_1bUF24AAAAC/fox-look.gif", "https://i.pinimg.com/originals/34/18/76/3418764243e784fc7e2402d59d5673be.gif", "https://i.gifer.com/origin/b0/b06ebfe63d1feebcf70ba3e5c145dd72_w200.gif", "https://thumbs.gfycat.com/BaggyHeftyFly-size_restricted.gif", "https://i.gifer.com/origin/c4/c47064a771f87bece949d1572b350c78.gif", "https://i.gifer.com/origin/d1/d1fdc742d9f69e3275a9bb744c819253_w200.gif", "https://vgif.ru/gifs/155/vgif-ru-26435.gif", "https://cs10.pikabu.ru/post_img/2018/07/20/5/1532071938166991608.gif", "https://vgif.ru/gifs/155/vgif-ru-26435.gif", "https://media.tenor.com/rJBaF7NSrygAAAAC/fuu-gadost.gif", "https://i.pinimg.com/originals/84/61/68/8461684797d18225f33e0a0bc62cd0e3.gif", "https://media.tenor.com/m_bhW_MGcPUAAAAC/fox-%D0%BB%D0%B8%D1%81%D0%B0.gif", "https://vgif.ru/gifs/161/vgif-ru-34388.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Fox**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(fox)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="fox", description="Рандомная картинка с ( fox )")
async def fox (ctx, *, text=None):
    fox = ["https://media.tenor.com/pdiR_1bUF24AAAAC/fox-look.gif", "https://i.pinimg.com/originals/34/18/76/3418764243e784fc7e2402d59d5673be.gif", "https://i.gifer.com/origin/b0/b06ebfe63d1feebcf70ba3e5c145dd72_w200.gif", "https://thumbs.gfycat.com/BaggyHeftyFly-size_restricted.gif", "https://i.gifer.com/origin/c4/c47064a771f87bece949d1572b350c78.gif", "https://i.gifer.com/origin/d1/d1fdc742d9f69e3275a9bb744c819253_w200.gif", "https://vgif.ru/gifs/155/vgif-ru-26435.gif", "https://cs10.pikabu.ru/post_img/2018/07/20/5/1532071938166991608.gif", "https://vgif.ru/gifs/155/vgif-ru-26435.gif", "https://media.tenor.com/rJBaF7NSrygAAAAC/fuu-gadost.gif", "https://i.pinimg.com/originals/84/61/68/8461684797d18225f33e0a0bc62cd0e3.gif", "https://media.tenor.com/m_bhW_MGcPUAAAAC/fox-%D0%BB%D0%B8%D1%81%D0%B0.gif", "https://vgif.ru/gifs/161/vgif-ru-34388.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с fox**')
        emb1.set_image(url=f'{random.choice(fox)}')
        await ctx.send(embed=emb1)

@bot.command()
async def wolf (ctx, *, text=None):
    wolf = ["https://media.tenor.com/JpcVkuH0AHUAAAAd/wolf-howling-wolf.gif", "https://media4.giphy.com/media/fnix5judzLJDJTaLgm/giphy.gif", "https://media.tenor.com/ltpyiPEvEE0AAAAM/magic-wolf.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fb577e15-b84a-4666-bbaf-d5760729c8e5/d9ek9s4-0c2c2684-81d3-42dd-8fd9-d7d439f6df2d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ZiNTc3ZTE1LWI4NGEtNDY2Ni1iYmFmLWQ1NzYwNzI5YzhlNVwvZDllazlzNC0wYzJjMjY4NC04MWQzLTQyZGQtOGZkOS1kN2Q0MzlmNmRmMmQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.k5gez4PP_S5p7Kx-DNkLk-ra813UElCk99n2C4CWeSk", "https://media4.giphy.com/media/1QiMXaDe9cKFlL0T1d/giphy.gif", "https://media.tenor.com/1Veo6AAmQk4AAAAC/alpha-wolf.gif", "https://www.gifcen.com/wp-content/uploads/2022/05/wolf-gif-10.gif", "https://img1.picmix.com/output/pic/normal/1/3/6/0/10130631_c55dc.gif", "https://media.tenor.com/Ktyyo6gk0R4AAAAd/wolf-kiss-wolf.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c83856a4-c236-472b-a3ea-304d4c2a48f1/dd44ayv-c19f916e-48ca-429c-86a5-b9f5894af43c.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M4Mzg1NmE0LWMyMzYtNDcyYi1hM2VhLTMwNGQ0YzJhNDhmMVwvZGQ0NGF5di1jMTlmOTE2ZS00OGNhLTQyOWMtODZhNS1iOWY1ODk0YWY0M2MuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.nn97WM4WsnHOWzulq_-bPzgyJ5eDiDUEpOMwFeRMth8", "https://art.pixilart.com/e9287417586d848.gif", "https://www.icegif.com/wp-content/uploads/2022/09/icegif-1303.gif", "https://steamuserimages-a.akamaihd.net/ugc/871867316815948620/CA5351FFCB4A2547314BFEEB70FA54BADA709407/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Wolf**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(wolf)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="wolf", description="Рандомная картинка с ( wolf )")
async def wolf (ctx, *, text=None):
    wolf = ["https://media.tenor.com/JpcVkuH0AHUAAAAd/wolf-howling-wolf.gif", "https://media4.giphy.com/media/fnix5judzLJDJTaLgm/giphy.gif", "https://media.tenor.com/ltpyiPEvEE0AAAAM/magic-wolf.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fb577e15-b84a-4666-bbaf-d5760729c8e5/d9ek9s4-0c2c2684-81d3-42dd-8fd9-d7d439f6df2d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ZiNTc3ZTE1LWI4NGEtNDY2Ni1iYmFmLWQ1NzYwNzI5YzhlNVwvZDllazlzNC0wYzJjMjY4NC04MWQzLTQyZGQtOGZkOS1kN2Q0MzlmNmRmMmQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.k5gez4PP_S5p7Kx-DNkLk-ra813UElCk99n2C4CWeSk", "https://media4.giphy.com/media/1QiMXaDe9cKFlL0T1d/giphy.gif", "https://media.tenor.com/1Veo6AAmQk4AAAAC/alpha-wolf.gif", "https://www.gifcen.com/wp-content/uploads/2022/05/wolf-gif-10.gif", "https://img1.picmix.com/output/pic/normal/1/3/6/0/10130631_c55dc.gif", "https://media.tenor.com/Ktyyo6gk0R4AAAAd/wolf-kiss-wolf.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c83856a4-c236-472b-a3ea-304d4c2a48f1/dd44ayv-c19f916e-48ca-429c-86a5-b9f5894af43c.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M4Mzg1NmE0LWMyMzYtNDcyYi1hM2VhLTMwNGQ0YzJhNDhmMVwvZGQ0NGF5di1jMTlmOTE2ZS00OGNhLTQyOWMtODZhNS1iOWY1ODk0YWY0M2MuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.nn97WM4WsnHOWzulq_-bPzgyJ5eDiDUEpOMwFeRMth8", "https://art.pixilart.com/e9287417586d848.gif", "https://www.icegif.com/wp-content/uploads/2022/09/icegif-1303.gif", "https://steamuserimages-a.akamaihd.net/ugc/871867316815948620/CA5351FFCB4A2547314BFEEB70FA54BADA709407/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с wolf**')
        emb1.set_image(url=f'{random.choice(wolf)}')
        await ctx.send(embed=emb1)

@bot.command()
async def xxxtentacion (ctx, *, text=None):
    xxxtentacion = ["https://thumbs.gfycat.com/LongClosedEnglishsetter-size_restricted.gif", "https://media.tenor.com/e0mI7E23NdcAAAAd/xxx-tentacion.gif", "https://media.tenor.com/5mVZmoyLeYUAAAAC/dude-with-a-big-xxx-tentacion.gif", "https://i.gifer.com/origin/40/4044c1cc3d9a524d3d5372524f93b8f9.gif", "https://media.tenor.com/l2EGhAl3NREAAAAC/xxxtentacion-money.gif", "https://www.icegif.com/wp-content/uploads/2022/09/icegif-138.gif", "https://i.pinimg.com/originals/c2/c0/15/c2c01571259439d98728e03dd27f7d75.gif", "https://i.gifer.com/origin/a8/a8fa366025739dd266129183929ebddf_w200.gif", "https://media.tenor.com/kKeYlbdm7UsAAAAC/xxx-tentacion-peace-out.gif", "https://thumbs.gfycat.com/FlusteredMadArizonaalligatorlizard-size_restricted.gif", "https://gifdb.com/images/high/xxxtentacion-head-banging-car-4urx423lr0ezmss0.gif", "https://thumbs.gfycat.com/EducatedPastGar-size_restricted.gif", "https://thumbs.gfycat.com/ZigzagConventionalInchworm-max-1mb.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с XXXTENTACION**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(xxxtentacion)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="xxxtentacion", description="Рандомная картинка с ( xxxtentacion )")
async def xxxtentacion (ctx, *, text=None):
    xxxtentacion = ["https://thumbs.gfycat.com/LongClosedEnglishsetter-size_restricted.gif", "https://media.tenor.com/e0mI7E23NdcAAAAd/xxx-tentacion.gif", "https://media.tenor.com/5mVZmoyLeYUAAAAC/dude-with-a-big-xxx-tentacion.gif", "https://i.gifer.com/origin/40/4044c1cc3d9a524d3d5372524f93b8f9.gif", "https://media.tenor.com/l2EGhAl3NREAAAAC/xxxtentacion-money.gif", "https://www.icegif.com/wp-content/uploads/2022/09/icegif-138.gif", "https://i.pinimg.com/originals/c2/c0/15/c2c01571259439d98728e03dd27f7d75.gif", "https://i.gifer.com/origin/a8/a8fa366025739dd266129183929ebddf_w200.gif", "https://media.tenor.com/kKeYlbdm7UsAAAAC/xxx-tentacion-peace-out.gif", "https://thumbs.gfycat.com/FlusteredMadArizonaalligatorlizard-size_restricted.gif", "https://gifdb.com/images/high/xxxtentacion-head-banging-car-4urx423lr0ezmss0.gif", "https://thumbs.gfycat.com/EducatedPastGar-size_restricted.gif", "https://thumbs.gfycat.com/ZigzagConventionalInchworm-max-1mb.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с xxxtentacion**')
        emb1.set_image(url=f'{random.choice(xxxtentacion)}')
        await ctx.send(embed=emb1)

@bot.command()
async def trippie (ctx, *, text=None):
    trippie = ["https://media.tenor.com/20cga8-qXzcAAAAC/really-trippie-redd.gif", "https://thumbs.gfycat.com/ShockedCostlyBellsnake-max-1mb.gif", "https://media.tenor.com/MG42kWrwuPwAAAAC/trippie-redd-trippie.gif", "https://media.tenor.com/dW1QYsFOIlwAAAAM/trippie-redd.gif", "https://i.pinimg.com/originals/b3/d0/a3/b3d0a3ed5ce9270c2027d9ce0a681549.gif", "https://thumbs.gfycat.com/AgonizingSmallBaboon-max-1mb.gif", "https://media.tenor.com/yDiE5ScgxkAAAAAM/trippieredd-trippie.gif", "https://i.pinimg.com/originals/27/71/2f/27712f82209e1005eb5b5f155fe819e1.gif", "https://thumbs.gfycat.com/FarawayHauntingAchillestang-max-1mb.gif", "https://thumbs.gfycat.com/RightGleefulBeardedcollie-size_restricted.gif", "https://gifdb.com/images/high/trippie-redd-shooting-himself-qtfb78hx79nv3t10.gif", "https://media.tenor.com/XrN5FzhImTcAAAAM/trippie-redd-digibyte.gif", "https://thumbs.gfycat.com/FineMilkyCub-size_restricted.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Trippie Red**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(trippie)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="trippie", description="Рандомная картинка с ( trippie )")
async def trippie (ctx, *, text=None):
    trippie = ["https://media.tenor.com/20cga8-qXzcAAAAC/really-trippie-redd.gif", "https://thumbs.gfycat.com/ShockedCostlyBellsnake-max-1mb.gif", "https://media.tenor.com/MG42kWrwuPwAAAAC/trippie-redd-trippie.gif", "https://media.tenor.com/dW1QYsFOIlwAAAAM/trippie-redd.gif", "https://i.pinimg.com/originals/b3/d0/a3/b3d0a3ed5ce9270c2027d9ce0a681549.gif", "https://thumbs.gfycat.com/AgonizingSmallBaboon-max-1mb.gif", "https://media.tenor.com/yDiE5ScgxkAAAAAM/trippieredd-trippie.gif", "https://i.pinimg.com/originals/27/71/2f/27712f82209e1005eb5b5f155fe819e1.gif", "https://thumbs.gfycat.com/FarawayHauntingAchillestang-max-1mb.gif", "https://thumbs.gfycat.com/RightGleefulBeardedcollie-size_restricted.gif", "https://gifdb.com/images/high/trippie-redd-shooting-himself-qtfb78hx79nv3t10.gif", "https://media.tenor.com/XrN5FzhImTcAAAAM/trippie-redd-digibyte.gif", "https://thumbs.gfycat.com/FineMilkyCub-size_restricted.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с trippie**')
        emb1.set_image(url=f'{random.choice(trippie)}')
        await ctx.send(embed=emb1)

@bot.command()
async def rabbit (ctx, *, text=None):
    rabbit = ["https://media.tenor.com/I50aFOQrLNoAAAAM/bunny-bunny-rabbit.gif", "https://media.tenor.com/8RARhGNaClQAAAAM/funny-bunny-confused-bunny.gif", "https://media2.giphy.com/media/WiXMlla4ZFR8Q/giphy.gif", "https://media.tenor.com/q_jj1u340XAAAAAd/snowball-bunny-carrot.gif", "https://upload.wikimedia.org/wikipedia/commons/b/b1/Rabbit.gif", "https://media1.giphy.com/media/qca5DjHlDzhrW/giphy.gif", "https://media.tenor.com/eZnsExPPMMsAAAAM/blacrswan.gif", "https://media.tenor.com/dVcOPVRtBaYAAAAd/bunny-rofl.gif", "https://media.tenor.com/QrE7Lq_rxA0AAAAM/snow-ball-rabbit.gif", "https://i.pinimg.com/originals/6d/85/d0/6d85d028794fdc71d19bb40ce21d1f43.gif", "https://www.icegif.com/wp-content/uploads/rabbit-icegif.gif", "http://24.media.tumblr.com/tumblr_m96cshZtyx1rqkghxo1_500.gif", "https://media2.giphy.com/media/LZSg0Ka2FlcFUm2o03/200w.gif?cid=6c09b952e1tjkt1e9rfnouq5l7a6lv0fn3mmfp5glpn5mpb9&rid=200w.gif&ct=g"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Rabbit**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(rabbit)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="rabbit", description="Рандомная картинка с ( rabbit )")
async def rabbit (ctx, *, text=None):
    rabbit = ["https://media.tenor.com/I50aFOQrLNoAAAAM/bunny-bunny-rabbit.gif", "https://media.tenor.com/8RARhGNaClQAAAAM/funny-bunny-confused-bunny.gif", "https://media2.giphy.com/media/WiXMlla4ZFR8Q/giphy.gif", "https://media.tenor.com/q_jj1u340XAAAAAd/snowball-bunny-carrot.gif", "https://upload.wikimedia.org/wikipedia/commons/b/b1/Rabbit.gif", "https://media1.giphy.com/media/qca5DjHlDzhrW/giphy.gif", "https://media.tenor.com/eZnsExPPMMsAAAAM/blacrswan.gif", "https://media.tenor.com/dVcOPVRtBaYAAAAd/bunny-rofl.gif", "https://media.tenor.com/QrE7Lq_rxA0AAAAM/snow-ball-rabbit.gif", "https://i.pinimg.com/originals/6d/85/d0/6d85d028794fdc71d19bb40ce21d1f43.gif", "https://www.icegif.com/wp-content/uploads/rabbit-icegif.gif", "http://24.media.tumblr.com/tumblr_m96cshZtyx1rqkghxo1_500.gif", "https://media2.giphy.com/media/LZSg0Ka2FlcFUm2o03/200w.gif?cid=6c09b952e1tjkt1e9rfnouq5l7a6lv0fn3mmfp5glpn5mpb9&rid=200w.gif&ct=g"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с rabbit**')
        emb1.set_image(url=f'{random.choice(rabbit)}')
        await ctx.send(embed=emb1)

@bot.command()
async def yzhik (ctx, *, text=None):
    yzhik = ["https://media.tenor.com/_0CKYTCvTswAAAAd/%D0%B5%D0%B6-%D0%B5%D1%81%D1%82.gif", "https://i.gifer.com/origin/63/639409a599a11868cc07a3723daf5f20_w200.gif", "https://i.gifer.com/origin/f7/f75964815da1b04b17c4a9b34458fea3_w200.gif", "https://media.tenor.com/FVm1EN4ly1gAAAAC/cute-hedgehog.gif", "https://i.pinimg.com/originals/5e/43/b4/5e43b498ddb4891798074a6edeeda290.gif", "https://i.gifer.com/origin/83/834ef8356ad20d26f9f302c808fd3bab_w200.gif", "https://thumbs.gfycat.com/AgreeableLikelyCentipede-size_restricted.gif", "https://media.tenor.com/muf2ttWVtGAAAAAd/hedgehog-%D0%B5%D0%B6%D0%B8%D0%BA.gif", "https://s00.yaplakal.com/pics/pics_original/3/5/6/1227653.gif", "https://media.tenor.com/KYb5vrA-lDUAAAAC/%D0%B5%D0%B6-%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B6%D1%83.gif", "https://media.tenor.com/0KONuduxh4YAAAAC/%D0%B5%D0%B6-%D1%91%D0%B6.gif", "https://cs9.pikabu.ru/post_img/2017/05/18/5/1495093179135792708.gif", "https://i.pinimg.com/originals/e6/08/77/e608778e0d93ea33e7536259b255432f.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Ыжик**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yzhik)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="yzhik", description="Рандомная картинка с ( yzhik )")
async def yzhik (ctx, *, text=None):
    yzhik = ["https://media.tenor.com/_0CKYTCvTswAAAAd/%D0%B5%D0%B6-%D0%B5%D1%81%D1%82.gif", "https://i.gifer.com/origin/63/639409a599a11868cc07a3723daf5f20_w200.gif", "https://i.gifer.com/origin/f7/f75964815da1b04b17c4a9b34458fea3_w200.gif", "https://media.tenor.com/FVm1EN4ly1gAAAAC/cute-hedgehog.gif", "https://i.pinimg.com/originals/5e/43/b4/5e43b498ddb4891798074a6edeeda290.gif", "https://i.gifer.com/origin/83/834ef8356ad20d26f9f302c808fd3bab_w200.gif", "https://thumbs.gfycat.com/AgreeableLikelyCentipede-size_restricted.gif", "https://media.tenor.com/muf2ttWVtGAAAAAd/hedgehog-%D0%B5%D0%B6%D0%B8%D0%BA.gif", "https://s00.yaplakal.com/pics/pics_original/3/5/6/1227653.gif", "https://media.tenor.com/KYb5vrA-lDUAAAAC/%D0%B5%D0%B6-%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B6%D1%83.gif", "https://media.tenor.com/0KONuduxh4YAAAAC/%D0%B5%D0%B6-%D1%91%D0%B6.gif", "https://cs9.pikabu.ru/post_img/2017/05/18/5/1495093179135792708.gif", "https://i.pinimg.com/originals/e6/08/77/e608778e0d93ea33e7536259b255432f.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с yzhik**')
        emb1.set_image(url=f'{random.choice(yzhik)}')
        await ctx.send(embed=emb1)

@bot.command()
async def lilnasx (ctx, *, text=None):
    lilnasx = ["https://media0.giphy.com/media/qJGVmfgnvPi3dfxyJu/200w.gif", "https://thumbs.gfycat.com/PassionateOldHarrierhawk-size_restricted.gif", "https://thumbs.gfycat.com/ThoughtfulUnkemptAfricanaugurbuzzard-max-1mb.gif", "https://media.tenor.com/hhgT8YfNvr8AAAAM/posing-glam.gif", "https://media0.giphy.com/media/wgXbxE62wnubMrZHWP/200w.gif", "https://media1.giphy.com/media/SDDWlKL9mussXKDKr1/200w.gif", "https://media.tenor.com/g0K3BISVadgAAAAM/lil-nas-x.gif", "https://thumbs.gfycat.com/AdorableLeanHerald-size_restricted.gif", "https://donttakefake.com/wp-content/uploads/2021/04/Lil-Nas-X-Montero-dtf-magazine-3.gif", "https://images.spletnik.ru/i/F/F0YN0AIw0B/1011.gif", "https://www.spletnik.ru/img/2021/10/nadja/lilnasx/20211007-nas-8.gif", "https://media.giphy.com/media/e4iNOYWssyGQamrD4l/giphy.gif?cid=790b7611f950203dc65852b0dce57e7d8b7478b931bbbddf&rid=giphy.gif", "https://thred.com/wp-content/uploads/icoolkidimages/giphy_14_1.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Lil Nas X**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(lilnasx)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="lilnasx", description="Рандомная картинка с ( lilnasx )")
async def lilnasx (ctx, *, text=None):
    lilnasx = ["https://media0.giphy.com/media/qJGVmfgnvPi3dfxyJu/200w.gif", "https://thumbs.gfycat.com/PassionateOldHarrierhawk-size_restricted.gif", "https://thumbs.gfycat.com/ThoughtfulUnkemptAfricanaugurbuzzard-max-1mb.gif", "https://media.tenor.com/hhgT8YfNvr8AAAAM/posing-glam.gif", "https://media0.giphy.com/media/wgXbxE62wnubMrZHWP/200w.gif", "https://media1.giphy.com/media/SDDWlKL9mussXKDKr1/200w.gif", "https://media.tenor.com/g0K3BISVadgAAAAM/lil-nas-x.gif", "https://thumbs.gfycat.com/AdorableLeanHerald-size_restricted.gif", "https://donttakefake.com/wp-content/uploads/2021/04/Lil-Nas-X-Montero-dtf-magazine-3.gif", "https://images.spletnik.ru/i/F/F0YN0AIw0B/1011.gif", "https://www.spletnik.ru/img/2021/10/nadja/lilnasx/20211007-nas-8.gif", "https://media.giphy.com/media/e4iNOYWssyGQamrD4l/giphy.gif?cid=790b7611f950203dc65852b0dce57e7d8b7478b931bbbddf&rid=giphy.gif", "https://thred.com/wp-content/uploads/icoolkidimages/giphy_14_1.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с lilnasx**')
        emb1.set_image(url=f'{random.choice(lilnasx)}')
        await ctx.send(embed=emb1)

@bot.command()
async def topic(ctx : nextcord.Member, *, text=None):
    topic = ["https://media.discordapp.net/attachments/980498827062673498/1070112746617704568/spin.gif"]
    author = ctx.message.author
    if text ==None:
        emb1 = nextcord.Embed(title='🥐 Тема', description=f'Пользователь {ctx.author.mention} хочет общаться!', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(topic)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="topic", description="Если у вас проблема с чатом")
async def topic (ctx, *, text=None):
    topic = ["https://media.discordapp.net/attachments/980498827062673498/1070112746617704568/spin.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='🥐 Тема', description=f'Я хочу общаться!')
        emb1.set_image(url=f'{random.choice(topic)}')
        await ctx.send(embed=emb1)

@bot.command()
async def tesla (ctx, *, text=None):
    tesla = ["https://media0.giphy.com/media/W6dorQn7tpRytTYmch/giphy.gif", "https://media.tenor.com/2Bn8Dj1Z3NgAAAAC/tesla-drifting.gif", "https://media3.giphy.com/media/xT39DhBvK92OIeFsVG/giphy.gif", "https://media.tenor.com/kcjejaZcTKkAAAAC/tesla.gif", "https://thumbs.gfycat.com/AssuredSilkyCooter-size_restricted.gif", "https://thumbs.gfycat.com/CanineMemorableBudgie-max-1mb.gif", "https://i.gifer.com/6h6.gif", "https://i.pinimg.com/originals/8d/3e/59/8d3e59ec2f19a8794fc89541929b59da.gif", "https://www.teslarati.com/wp-content/uploads/2018/10/tesla-family-gif.gif", "https://media4.giphy.com/media/WtUiSnHGtEPOLQT80x/giphy.gif", "https://i.gifer.com/6h9.gif", "https://media.tenor.com/2aAgfmaGuk8AAAAC/tesla-model-x.gif", "https://j.gifs.com/ZVyBrw.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с Tesla**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(tesla)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="tesla", description="Рандомная картинка с ( tesla )")
async def tesla (ctx, *, text=None):
    tesla = ["https://media0.giphy.com/media/W6dorQn7tpRytTYmch/giphy.gif", "https://media.tenor.com/2Bn8Dj1Z3NgAAAAC/tesla-drifting.gif", "https://media3.giphy.com/media/xT39DhBvK92OIeFsVG/giphy.gif", "https://media.tenor.com/kcjejaZcTKkAAAAC/tesla.gif", "https://thumbs.gfycat.com/AssuredSilkyCooter-size_restricted.gif", "https://thumbs.gfycat.com/CanineMemorableBudgie-max-1mb.gif", "https://i.gifer.com/6h6.gif", "https://i.pinimg.com/originals/8d/3e/59/8d3e59ec2f19a8794fc89541929b59da.gif", "https://www.teslarati.com/wp-content/uploads/2018/10/tesla-family-gif.gif", "https://media4.giphy.com/media/WtUiSnHGtEPOLQT80x/giphy.gif", "https://i.gifer.com/6h9.gif", "https://media.tenor.com/2aAgfmaGuk8AAAAC/tesla-model-x.gif", "https://j.gifs.com/ZVyBrw.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'✨ **рандомная гифка/картинка с tesla**')
        emb1.set_image(url=f'{random.choice(tesla)}')
        await ctx.send(embed=emb1)

@bot.command(usage="[RolePlay]")
async def hug (ctx, member : nextcord.Member, *, text=None):
    hug = ["https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif", "https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif", "https://c.tenor.com/uIBg3BLATf0AAAAC/hug-darker.gif", "https://c.tenor.com/ncblDAj_2FwAAAAC/abrazo-hug.gif", "https://c.tenor.com/QCQV57yhBMsAAAAd/comforting-hug.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'👐 {ctx.author.mention} **обнял(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(hug)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👐 {ctx.author.mention} **обняла(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(hug)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="hug", description="Обнять пользователя")
async def hug (interaction : Interaction, member : nextcord.Member, *, text=None):
    hug = ["https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif", "https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif", "https://c.tenor.com/uIBg3BLATf0AAAAC/hug-darker.gif", "https://c.tenor.com/ncblDAj_2FwAAAAC/abrazo-hug.gif", "https://c.tenor.com/QCQV57yhBMsAAAAd/comforting-hug.gif"]
    if text ==None:
        emb1 = nextcord.Embed(title='', description=f'👐 Вы **обняли** {member.mention}')
        emb1.set_image(url=f'{random.choice(hug)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👐 Вы **обнялаи** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(hug)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="RolePLay")
async def slap (ctx, member : nextcord.Member, *, text=None):
    slap = ["https://c.tenor.com/1lJTSPaUfKkAAAAd/chika-fujiwara-fwap.gif", "https://c.tenor.com/1-1M4PZpYcMAAAAd/tsuki-tsuki-ga.gif", "https://c.tenor.com/E4Px9kJOQ5wAAAAC/anime-kid.gif", "https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif", "https://c.tenor.com/wOCOTBGZJyEAAAAC/chikku-neesan-girl-hit-wall.gif", "https://tenor.com/view/saki-saki-kanojo-mo-kanojo-kmk-saki-anime-gif-22206764"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🖐 {ctx.author.mention} **ударил(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(slap)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🖐 {ctx.author.mention} **ударил(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(slap)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="slap", description="Ударить пользователя")
async def slap (interaction : Interaction, member : nextcord.Member, *, text=None):
    slap = ["https://c.tenor.com/1lJTSPaUfKkAAAAd/chika-fujiwara-fwap.gif", "https://c.tenor.com/1-1M4PZpYcMAAAAd/tsuki-tsuki-ga.gif", "https://c.tenor.com/E4Px9kJOQ5wAAAAC/anime-kid.gif", "https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif", "https://c.tenor.com/wOCOTBGZJyEAAAAC/chikku-neesan-girl-hit-wall.gif", "https://tenor.com/view/saki-saki-kanojo-mo-kanojo-kmk-saki-anime-gif-22206764"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🖐 Вы **ударили** {member.mention}')
        emb1.set_image(url=f'{random.choice(slap)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🖐 Вы **ударили** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(slap)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def kiss (ctx, member : nextcord.Member, *, text=None):
    kiss = ["https://c.tenor.com/VTvkMN6P648AAAAC/anime-kiss.gif", "https://c.tenor.com/16MBIsjDDYcAAAAC/love-cheek.gif", "https://c.tenor.com/Ge4DoX5aDD0AAAAC/love-kiss.gif", "https://c.tenor.com/JQ9jjb_JTqEAAAAC/anime-kiss.gif", "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'❤️ {ctx.author.mention} **поцеловал(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(kiss)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'❤️ {ctx.author.mention} **поцеловал(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(kiss)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="kiss", description="Поцеловать пользователя")
async def kiss (interaction : Interaction, member : nextcord.Member, *, text=None):
    kiss = ["https://c.tenor.com/VTvkMN6P648AAAAC/anime-kiss.gif", "https://c.tenor.com/16MBIsjDDYcAAAAC/love-cheek.gif", "https://c.tenor.com/Ge4DoX5aDD0AAAAC/love-kiss.gif", "https://c.tenor.com/JQ9jjb_JTqEAAAAC/anime-kiss.gif", "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'❤️ Вы **поцеловали** {member.mention}')
        emb1.set_image(url=f'{random.choice(kiss)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'❤️ Вы **поцеловали** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(kiss)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def lewd (ctx, member : nextcord.Member, *, text = None):
    lewd = ["https://c.tenor.com/2iEVFFCbPj4AAAAC/momokuri-anime-blush.gif", "https://c.tenor.com/Tk2xYonmrsEAAAAC/anime-blushing.gif", "https://c.tenor.com/bEes0xCurvMAAAAC/anime-blush-dizzy.gif", "https://c.tenor.com/HAWlr1X00Y8AAAAC/anime-love.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😊 {ctx.author.mention} **смущен(а) на** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(lewd)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😊 {ctx.author.mention} **смущен(а) на** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(lewd)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="lewd", description="Смутиться на пользователя")
async def lewd (interaction : Interaction, member : nextcord.Member, *, text = None):
    lewd = ["https://c.tenor.com/2iEVFFCbPj4AAAAC/momokuri-anime-blush.gif", "https://c.tenor.com/Tk2xYonmrsEAAAAC/anime-blushing.gif", "https://c.tenor.com/bEes0xCurvMAAAAC/anime-blush-dizzy.gif", "https://c.tenor.com/HAWlr1X00Y8AAAAC/anime-love.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😊 Вы **смущены на** {member.mention}')
        emb1.set_image(url=f'{random.choice(lewd)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😊 Вы **смущены на** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(lewd)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def angry (ctx, member : nextcord.Member, *, text = None):
    angry = ["https://c.tenor.com/-aieB6Qw8YQAAAAd/anime-angry.gif", "https://c.tenor.com/wtSs_VCHYmEAAAAC/noela-angry.gif", "https://c.tenor.com/jgFVzr3YeJwAAAAC/date-a-live-rage.gif", "https://c.tenor.com/B2G5s1cY7GUAAAAC/anime-angry.gif", "https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😠 {ctx.author.mention} **разозлен(а) на** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(angry)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😠 {ctx.author.mention} **разозлен(а) на** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(angry)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="angry", description="Злиться на пользователя")
async def angry (interaction : Interaction, member : nextcord.Member, *, text = None):
    angry = ["https://c.tenor.com/-aieB6Qw8YQAAAAd/anime-angry.gif", "https://c.tenor.com/wtSs_VCHYmEAAAAC/noela-angry.gif", "https://c.tenor.com/jgFVzr3YeJwAAAAC/date-a-live-rage.gif", "https://c.tenor.com/B2G5s1cY7GUAAAAC/anime-angry.gif", "https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😠 Вы **разозлены на** {member.mention}')
        emb1.set_image(url=f'{random.choice(angry)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😠 Вы **разозлены на** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(angry)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def kill (ctx, member : nextcord.Member, *, text = None):
    kill = ["https://i.waifu.pics/ETWB-ef.gif", "https://i.waifu.pics/OByL0MA.gif", "https://i.waifu.pics/7Z1tV23.gif", "https://i.waifu.pics/hGFuwrQ.gif", "https://i.waifu.pics/judBJyS.gif", "https://i.waifu.pics/lgsRSai.gif", "https://i.waifu.pics/8uhQSdY.gif", "https://i.waifu.pics/hsAy9-u.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💀 {ctx.author.mention} **убил(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(kill)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💀 {ctx.author.mention} **убил(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(kill)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="kill", description="Убить пользователя")
async def kill (interaction : Interaction, member : nextcord.Member, *, text = None):
    kill = ["https://i.waifu.pics/ETWB-ef.gif", "https://i.waifu.pics/OByL0MA.gif", "https://i.waifu.pics/7Z1tV23.gif", "https://i.waifu.pics/hGFuwrQ.gif", "https://i.waifu.pics/judBJyS.gif", "https://i.waifu.pics/lgsRSai.gif", "https://i.waifu.pics/8uhQSdY.gif", "https://i.waifu.pics/hsAy9-u.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💀 Вы **убили** {member.mention}')
        emb1.set_image(url=f'{random.choice(kill)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'💀 Вы **убили** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(kill)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def poke (ctx, member : nextcord.Member, *, text = None):
    poke = ["https://i.waifu.pics/JlDu4xg.gif", "https://i.waifu.pics/vF1NIJu.gif", "https://i.waifu.pics/beT0l4e.gif", "https://i.waifu.pics/8L~QGTf.gif", "https://i.waifu.pics/Yf8glJM.gif", "https://i.waifu.pics/i2mQiAk.gif", "https://i.waifu.pics/1YxdKac.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👉 {ctx.author.mention} **тыкнул(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(poke)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👉 {ctx.author.mention} **тыкнул(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(poke)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="poke", description="Тыкнуть пользователя")
async def poke (interaction : Interaction, member : nextcord.Member, *, text = None):
    poke = ["https://i.waifu.pics/JlDu4xg.gif", "https://i.waifu.pics/vF1NIJu.gif", "https://i.waifu.pics/beT0l4e.gif", "https://i.waifu.pics/8L~QGTf.gif", "https://i.waifu.pics/Yf8glJM.gif", "https://i.waifu.pics/i2mQiAk.gif", "https://i.waifu.pics/1YxdKac.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👉 Вы **тыкнули** {member.mention}')
        emb1.set_image(url=f'{random.choice(poke)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👉 Вы **тыкнули** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(poke)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def pat (ctx, member : nextcord.Member, *, text = None):
    pat = ["https://i.waifu.pics/g~h0cvT.gif", "https://i.waifu.pics/pmOcanl.gif", "https://i.waifu.pics/0U6HeiX.gif", "https://i.waifu.pics/EE-BZm9.gif", "https://i.waifu.pics/jIPKD0Z.gif", "https://i.waifu.pics/J2EF9YT.gif", "https://i.waifu.pics/MGSjX0_.gif", "https://i.waifu.pics/nsvdMrv.gif", "https://i.waifu.pics/I~znmj2.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤗 {ctx.author.mention} **погладил(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(pat)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🤗 {ctx.author.mention} **погладил(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(pat)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="pat", description="Погладить пользователя")
async def pat (interaction : Interaction, member : nextcord.Member, *, text = None):
    pat = ["https://i.waifu.pics/g~h0cvT.gif", "https://i.waifu.pics/pmOcanl.gif", "https://i.waifu.pics/0U6HeiX.gif", "https://i.waifu.pics/EE-BZm9.gif", "https://i.waifu.pics/jIPKD0Z.gif", "https://i.waifu.pics/J2EF9YT.gif", "https://i.waifu.pics/MGSjX0_.gif", "https://i.waifu.pics/nsvdMrv.gif", "https://i.waifu.pics/I~znmj2.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤗 Вы **погладили** {member.mention}',)
        emb1.set_image(url=f'{random.choice(pat)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🤗 Вы **погладили** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(pat)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def bite (ctx, member : nextcord.Member, *, text = None):
    bite = ["https://i.waifu.pics/cnTLq9v.gif", "https://i.waifu.pics/9WRtGbr.gif", "https://i.waifu.pics/UgYmj1t.gif", "https://i.waifu.pics/iErgSVO.gif", "https://i.waifu.pics/W0VmZno.gif", "https://i.waifu.pics/YTKHSD4.gif", "https://i.waifu.pics/PulivJk.gif", "https://i.waifu.pics/bKScj44.gif", "https://i.waifu.pics/asvURcX.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😈 {ctx.author.mention} **укусил(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(bite)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😈 {ctx.author.mention} **укусил(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(bite)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="bite", description="Укусить пользователя")
async def bite (interaction : Interaction, member : nextcord.Member, *, text = None):
    bite = ["https://i.waifu.pics/cnTLq9v.gif", "https://i.waifu.pics/9WRtGbr.gif", "https://i.waifu.pics/UgYmj1t.gif", "https://i.waifu.pics/iErgSVO.gif", "https://i.waifu.pics/W0VmZno.gif", "https://i.waifu.pics/YTKHSD4.gif", "https://i.waifu.pics/PulivJk.gif", "https://i.waifu.pics/bKScj44.gif", "https://i.waifu.pics/asvURcX.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😈 Вы **укусили** {member.mention}')
        emb1.set_image(url=f'{random.choice(bite)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😈 Вы **укусили** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(bite)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def feed (ctx, member : nextcord.Member, *, text=None):
    feed = ["https://i.waifu.pics/g6ISmbU.gif", "https://i.waifu.pics/on3fsaG.gif", "https://i.waifu.pics/9cuZ2_c.gif", "https://i.waifu.pics/_Xhrs1u.gif", "https://i.waifu.pics/GfZNQ63.gif", "https://i.waifu.pics/v-zBxL0.gif", "https://i.waifu.pics/4Kqzf3o.gif", "https://i.waifu.pics/FJyxFzB.gif", "https://i.waifu.pics/-OvwPE6.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍕 {ctx.author.mention} **покормил(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(feed)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍕 {ctx.author.mention} **покормил(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(feed)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="feed", description="Покормить пользователя")
async def feed (interaction : Interaction, member : nextcord.Member, *, text=None):
    feed = ["https://i.waifu.pics/g6ISmbU.gif", "https://i.waifu.pics/on3fsaG.gif", "https://i.waifu.pics/9cuZ2_c.gif", "https://i.waifu.pics/_Xhrs1u.gif", "https://i.waifu.pics/GfZNQ63.gif", "https://i.waifu.pics/v-zBxL0.gif", "https://i.waifu.pics/4Kqzf3o.gif", "https://i.waifu.pics/FJyxFzB.gif", "https://i.waifu.pics/-OvwPE6.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍕 Вы **покормили** {member.mention}')
        emb1.set_image(url=f'{random.choice(feed)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍕 Вы **покормили** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(feed)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def smile (ctx, member : nextcord.Member, *, text = None):
    smile = ["https://i.waifu.pics/7lhMNMV.gif", "https://i.waifu.pics/u8drjx7.gif", "https://i.waifu.pics/4RMgMWL.gif", "https://i.waifu.pics/tvSCzkl.gif", "https://i.waifu.pics/MGiBjN-.gif", "https://i.waifu.pics/Uvqo6Mz.gif", "https://i.waifu.pics/mhLpKn5.gif", "https://i.waifu.pics/jGcj2CQ.gif", "https://i.waifu.pics/73ri7VG.gif", "https://i.waifu.pics/xyuju7Q.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🙂 {ctx.author.mention} **улыбнулся(ась) перед** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(smile)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🙂 {ctx.author.mention} **улыбнулся(ась)** перед {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(smile)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="smile", description="Улыбнуться перед пользователем")
async def smile (interaction : Interaction, member : nextcord.Member, *, text = None):
    smile = ["https://i.waifu.pics/7lhMNMV.gif", "https://i.waifu.pics/u8drjx7.gif", "https://i.waifu.pics/4RMgMWL.gif", "https://i.waifu.pics/tvSCzkl.gif", "https://i.waifu.pics/MGiBjN-.gif", "https://i.waifu.pics/Uvqo6Mz.gif", "https://i.waifu.pics/mhLpKn5.gif", "https://i.waifu.pics/jGcj2CQ.gif", "https://i.waifu.pics/73ri7VG.gif", "https://i.waifu.pics/xyuju7Q.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🙂 Вы **улыбнулись перед** {member.mention}')
        emb1.set_image(url=f'{random.choice(smile)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🙂 Вы **улыбнулись** перед {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(smile)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def lick (ctx, member : nextcord.Member, *, text = None):
    lick = ["https://c.tenor.com/4U2-K7XUIJUAAAAC/pain-ellenoar.gif", "https://c.tenor.com/uw6-q_y4xKsAAAAd/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5-darling-in-the-franxx.gif", "https://i.waifu.pics/iL8UVFd.gif", "https://i.waifu.pics/hV9cyEJ.gif", "https://c.tenor.com/0LMxPQdFBKAAAAAC/nekopara-kiss.gif", "https://i.waifu.pics/LyVaHfl.gif", "https://i.waifu.pics/JxQolYt.gif", "https://i.waifu.pics/at~DQwu.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😛 {ctx.author.mention} **облизал(а)** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(lick)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😛 {ctx.author.mention} **облизал(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(lick)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="lick", description="Облизать пользователя")
async def lick (interaction : Interaction, member : nextcord.Member, *, text = None):
    lick = ["https://c.tenor.com/4U2-K7XUIJUAAAAC/pain-ellenoar.gif", "https://c.tenor.com/uw6-q_y4xKsAAAAd/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5-darling-in-the-franxx.gif", "https://i.waifu.pics/iL8UVFd.gif", "https://i.waifu.pics/hV9cyEJ.gif", "https://c.tenor.com/0LMxPQdFBKAAAAAC/nekopara-kiss.gif", "https://i.waifu.pics/LyVaHfl.gif", "https://i.waifu.pics/JxQolYt.gif", "https://i.waifu.pics/at~DQwu.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😛 Вы **облизали** {member.mention}')
        emb1.set_image(url=f'{random.choice(lick)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😛 Вы **облизали** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(lick)}')
        await (interaction.response.send_message(embed=emb))
    
@bot.command(usage="[RolePlay]")
async def wave (ctx, member : nextcord.Member, *, text = None):
    wave = ["https://i.waifu.pics/wyVFEi7.gif", "https://i.waifu.pics/SNR4nf5.gif", "https://i.waifu.pics/Jvi3~TN.gif", "https://i.waifu.pics/iC7niFP.gif", "https://i.waifu.pics/s3G5xJ0.gif", "https://i.waifu.pics/RtR0LFI.gif", "https://i.waifu.pics/KEPtqkH.gif", "https://i.waifu.pics/T0gfAdU.gif", "https://i.waifu.pics/8npsaf-.gif", "https://i.waifu.pics/l3_ObDa.gif", "https://i.waifu.pics/546M14t.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👋 {ctx.author.mention} **приветствует** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(wave)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👋 {ctx.author.mention} **приветствует** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(wave)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="wave", description="Приветствовать пользователя")
async def wave (interaction : Interaction, member : nextcord.Member, *, text = None):
    wave = ["https://i.waifu.pics/wyVFEi7.gif", "https://i.waifu.pics/SNR4nf5.gif", "https://i.waifu.pics/Jvi3~TN.gif", "https://i.waifu.pics/iC7niFP.gif", "https://i.waifu.pics/s3G5xJ0.gif", "https://i.waifu.pics/RtR0LFI.gif", "https://i.waifu.pics/KEPtqkH.gif", "https://i.waifu.pics/T0gfAdU.gif", "https://i.waifu.pics/8npsaf-.gif", "https://i.waifu.pics/l3_ObDa.gif", "https://i.waifu.pics/546M14t.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👋 Вы **приветствуете** {member.mention}')
        emb1.set_image(url=f'{random.choice(wave)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👋 Вы **приветствуете** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(wave)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def yes (ctx : nextcord.Member, *, text = None):    
    yes = ["https://cdn.discordapp.com/attachments/736254151620820993/736254237205331978/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254245283561522/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254184617410580/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254228493893632/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254205492461568/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254202950582302/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254158205747270/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254266213138442/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254240372031496/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254234567376936/yes.gif"]
    auhor = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👍 {ctx.author.mention} **думает что всё круто!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yes)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="yes", description="Сказать 'Да'")
async def yes (interaction : Interaction, *, text = None):
    yes = ["https://cdn.discordapp.com/attachments/736254151620820993/736254237205331978/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254245283561522/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254184617410580/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254228493893632/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254205492461568/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254202950582302/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254158205747270/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254266213138442/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254240372031496/yes.gif", "https://cdn.discordapp.com/attachments/736254151620820993/736254234567376936/yes.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👍 **ты** думаешь что всё круто!')
        emb1.set_image(url=f'{random.choice(yes)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePlay]")
async def no (ctx : nextcord.Member, *, text = None):
    no = ["https://cdn.discordapp.com/attachments/736254603410014320/736254656174620742/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254607449128981/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/743053003820498964/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254633781231767/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254700134858883/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254733131579482/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254620514648114/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254652554936380/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254717839278100/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254644367654992/no.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👎 {ctx.author.mention} **не очень понравилось(**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(no)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="no", description="Сказать 'Нет'")
async def no (interaction : Interaction, *, text = None):
    no = ["https://cdn.discordapp.com/attachments/736254603410014320/736254656174620742/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254607449128981/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/743053003820498964/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254633781231767/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254700134858883/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254733131579482/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254620514648114/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254652554936380/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254717839278100/no.gif", "https://cdn.discordapp.com/attachments/736254603410014320/736254644367654992/no.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👎 **тебе** это не очень понравилось(')
        emb1.set_image(url=f'{random.choice(no)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def wink (ctx, member : nextcord.Member, *, text = None):
    wink = ["https://i.waifu.pics/QmF2rf1.gif", "https://i.waifu.pics/W4_OW_P.gif", "https://i.waifu.pics/zFUMzUA.gif", "https://i.waifu.pics/B9UEKY0.gif", "https://i.waifu.pics/B9UEKY0.gif", "https://i.waifu.pics/iUewj~j.gif", "https://i.waifu.pics/yhPnXdH.gif", "https://i.waifu.pics/pxAktJZ.gif", "https://i.waifu.pics/t2IcbQK.gif", "https://i.waifu.pics/YVzEB_9.gif", "https://i.waifu.pics/ydw2e2U.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😉 {ctx.author.mention} **подмигнул** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(wink)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😉 {ctx.author.mention} **подмигнул** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(wink)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="wink", description="Подмигнуть пользователю")
async def wink (interaction : Interaction, member : nextcord.Member, *, text = None):
    wink = ["https://i.waifu.pics/QmF2rf1.gif", "https://i.waifu.pics/W4_OW_P.gif", "https://i.waifu.pics/zFUMzUA.gif", "https://i.waifu.pics/B9UEKY0.gif", "https://i.waifu.pics/B9UEKY0.gif", "https://i.waifu.pics/iUewj~j.gif", "https://i.waifu.pics/yhPnXdH.gif", "https://i.waifu.pics/pxAktJZ.gif", "https://i.waifu.pics/t2IcbQK.gif", "https://i.waifu.pics/YVzEB_9.gif", "https://i.waifu.pics/ydw2e2U.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😉 **Вы** подмигнули {member.mention}')
        emb1.set_image(url=f'{random.choice(wink)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😉 **Вы** подмигнули {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(wink)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def cry (ctx : nextcord.Member, *, text = None):
    cry = ["https://i.waifu.pics/ABIGqvR.gif", "https://i.waifu.pics/ABIGqvR.gif", "https://i.waifu.pics/MT1xRHu.gif", "https://i.waifu.pics/q-3o-0e.gif", "https://i.waifu.pics/tfNqRJy.gif", "https://i.waifu.pics/WspRuww.gif", "https://i.waifu.pics/kmUKaHC.gif", "https://i.waifu.pics/~xVlJv7.gif", "https://i.waifu.pics/6x-~igD.gif", "https://i.waifu.pics/Rr~iaBU.gif", "https://i.waifu.pics/w~9Ts9z.gif", "https://i.waifu.pics/WspRuww.gif", "https://i.waifu.pics/USePcuV.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😢 {ctx.author.mention} **плачет...**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(cry)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="cry", description="Заплакать")
async def cry (interaction : Interaction, *, text = None):
    cry = ["https://i.waifu.pics/ABIGqvR.gif", "https://i.waifu.pics/ABIGqvR.gif", "https://i.waifu.pics/MT1xRHu.gif", "https://i.waifu.pics/q-3o-0e.gif", "https://i.waifu.pics/tfNqRJy.gif", "https://i.waifu.pics/WspRuww.gif", "https://i.waifu.pics/kmUKaHC.gif", "https://i.waifu.pics/~xVlJv7.gif", "https://i.waifu.pics/6x-~igD.gif", "https://i.waifu.pics/Rr~iaBU.gif", "https://i.waifu.pics/w~9Ts9z.gif", "https://i.waifu.pics/WspRuww.gif", "https://i.waifu.pics/USePcuV.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😢 **Вы** заплакали(')
        emb1.set_image(url=f'{random.choice(cry)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePlay]")
async def smug (ctx: nextcord.Member, *, text = None):
    smug = ["https://i.waifu.pics/1xhtYKR.gif", "https://i.waifu.pics/AegHHDx.gif", "https://i.waifu.pics/175w1G-.gif", "https://i.waifu.pics/t2jkJD0.gif", "https://i.waifu.pics/dT7J1xn.gif", "https://i.waifu.pics/jlVUvC7.gif", "https://i.waifu.pics/YXYR8LS.gif", "https://i.waifu.pics/YNyt3QN.gif", "https://i.waifu.pics/o71ra5G.gif", "https://i.waifu.pics/8Py2vAi.gif", "https://i.waifu.pics/PRXwZXJ.gif", "https://i.waifu.pics/I3ZnurL.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😊 {ctx.author.mention} **выглядит самодовольно**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(smug)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="smug", description="Выглядить самодовольно")
async def smug (interaction : Interaction, *, text = None):
    smug = ["https://i.waifu.pics/1xhtYKR.gif", "https://i.waifu.pics/AegHHDx.gif", "https://i.waifu.pics/175w1G-.gif", "https://i.waifu.pics/t2jkJD0.gif", "https://i.waifu.pics/dT7J1xn.gif", "https://i.waifu.pics/jlVUvC7.gif", "https://i.waifu.pics/YXYR8LS.gif", "https://i.waifu.pics/YNyt3QN.gif", "https://i.waifu.pics/o71ra5G.gif", "https://i.waifu.pics/8Py2vAi.gif", "https://i.waifu.pics/PRXwZXJ.gif", "https://i.waifu.pics/I3ZnurL.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😊 **Вы** выглядите самодовольно')
        emb1.set_image(url=f'{random.choice(smug)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def cuddle (ctx, member : nextcord.Member, *, text = None):
    cuddle = ["https://i.waifu.pics/zmpG5Rl.gif", "https://i.waifu.pics/AbvAa4m.gif", "https://i.waifu.pics/UAkc3_y.gif", "https://i.waifu.pics/~XVQpk0.gif", "https://i.waifu.pics/Kz_RkcY.gif", "https://i.waifu.pics/9o_qPSC.gif", "https://i.waifu.pics/~En9D5_.gif", "https://i.waifu.pics/xbLeRLK.gif", "https://i.waifu.pics/rGHo~vc.gif", "https://i.waifu.pics/qnlMuuF.gif", "https://i.waifu.pics/Uy5ga3F.gif", "https://i.waifu.pics/szHC1yJ.gif", "https://i.waifu.pics/AbvAa4m.gif", "https://i.waifu.pics/WSLUoer.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😛👐 {ctx.author.mention} **прижимается к** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(cuddle)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'😛👐 {ctx.author.mention} **прижимается к** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(cuddle)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="cuddle", description="Прижиматься к пользователю")
async def cuddle (interaction : Interaction, member : nextcord.Member, *, text = None):
    cuddle = ["https://i.waifu.pics/zmpG5Rl.gif", "https://i.waifu.pics/AbvAa4m.gif", "https://i.waifu.pics/UAkc3_y.gif", "https://i.waifu.pics/~XVQpk0.gif", "https://i.waifu.pics/Kz_RkcY.gif", "https://i.waifu.pics/9o_qPSC.gif", "https://i.waifu.pics/~En9D5_.gif", "https://i.waifu.pics/xbLeRLK.gif", "https://i.waifu.pics/rGHo~vc.gif", "https://i.waifu.pics/qnlMuuF.gif", "https://i.waifu.pics/Uy5ga3F.gif", "https://i.waifu.pics/szHC1yJ.gif", "https://i.waifu.pics/AbvAa4m.gif", "https://i.waifu.pics/WSLUoer.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😛👐 **Вы** прижимаетесь к {member.mention}')
        emb1.set_image(url=f'{random.choice(cuddle)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'😛👐 **Вы** прижимаетесь к {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(cuddle)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def dance (ctx: nextcord.Member, *, text = None):
    dance = ["https://i.waifu.pics/~4RnOPt.gif", "https://i.waifu.pics/V4ztx1j.gif", "https://i.waifu.pics/Rv-lh_B.gif", "https://i.waifu.pics/GNw8eK7.gif", "https://i.waifu.pics/dWcXWF0.gif", "https://i.waifu.pics/oI~t28j.gif", "https://i.waifu.pics/maB4-hQ.gif", "https://i.waifu.pics/P4PMK3m.gif", "https://i.waifu.pics/-J_3FPf.gif", "https://i.waifu.pics/YEG4YAl.gif", "https://i.waifu.pics/Fzhg8rD.gif", "https://i.waifu.pics/iVDuV9y.gif", "https://i.waifu.pics/YTiV2fl.gif", "https://i.waifu.pics/mKuJrYc.gif", "https://i.waifu.pics/urWfg8X.gif", "https://i.waifu.pics/A6d9ug0.gif", "https://i.waifu.pics/d5J29kk.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💃 {ctx.author.mention} **танцует**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(dance)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="dance", description="Танцевать")
async def dance (interaction : Interaction, *, text = None):
    dance = ["https://i.waifu.pics/~4RnOPt.gif", "https://i.waifu.pics/V4ztx1j.gif", "https://i.waifu.pics/Rv-lh_B.gif", "https://i.waifu.pics/GNw8eK7.gif", "https://i.waifu.pics/dWcXWF0.gif", "https://i.waifu.pics/oI~t28j.gif", "https://i.waifu.pics/maB4-hQ.gif", "https://i.waifu.pics/P4PMK3m.gif", "https://i.waifu.pics/-J_3FPf.gif", "https://i.waifu.pics/YEG4YAl.gif", "https://i.waifu.pics/Fzhg8rD.gif", "https://i.waifu.pics/iVDuV9y.gif", "https://i.waifu.pics/YTiV2fl.gif", "https://i.waifu.pics/mKuJrYc.gif", "https://i.waifu.pics/urWfg8X.gif", "https://i.waifu.pics/A6d9ug0.gif", "https://i.waifu.pics/d5J29kk.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💃 **Вы** танцуете')
        emb1.set_image(url=f'{random.choice(dance)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def sing (ctx: nextcord.Member, *, text = None):
    sing = ["https://cdn.discordapp.com/attachments/874742187357773844/874743043486543872/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742945864110120/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742590652706918/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/881900344035123270/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/881900424075030528/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742504237436959/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742765756481576/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742690829443132/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742401061756928/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742229535699044/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742322699583538/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742863513157662/sing.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🎙 {ctx.author.mention} **поёт! Какой у тебя прекрасный голос!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(sing)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="sing", description="Сказать 'Нет'")
async def sing (interaction : Interaction, *, text = None):
    sing = ["https://cdn.discordapp.com/attachments/874742187357773844/874743043486543872/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742945864110120/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742590652706918/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/881900344035123270/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/881900424075030528/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742504237436959/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742765756481576/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742690829443132/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742401061756928/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742229535699044/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742322699583538/sing.gif", "https://cdn.discordapp.com/attachments/874742187357773844/874742863513157662/sing.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🎙 **Вы** поете! Какой у вас прекрасный голос!')
        emb1.set_image(url=f'{random.choice(sing)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def facepalm (ctx: nextcord.Member, *, text = None):
    facepalm = ["https://cdn.discordapp.com/attachments/736262744474517584/736262854734512188/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262819971858543/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262764284346428/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504295553957888/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262847973294171/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504311413276732/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504268996018186/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504257276477510/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262815425495142/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504350113857556/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504387749609492/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262842528825375/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262779408744509/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262859821940836/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504282911932486/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504375288201216/facepalm.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤦 {ctx.author.mention} **ему очень стыдно!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(facepalm)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="facepalm", description="Испанский стыд")
async def facepalm (interaction : Interaction, *, text = None):
    facepalm = ["https://cdn.discordapp.com/attachments/736262744474517584/736262854734512188/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262819971858543/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262764284346428/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504295553957888/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262847973294171/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504311413276732/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504268996018186/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504257276477510/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262815425495142/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504350113857556/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504387749609492/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262842528825375/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262779408744509/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/736262859821940836/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504282911932486/facepalm.gif", "https://cdn.discordapp.com/attachments/736262744474517584/834504375288201216/facepalm.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤦‍♀️ **Тебе** очень стыдно!')
        emb1.set_image(url=f'{random.choice(facepalm)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def jump (ctx: nextcord.Member, *, text = None):
    jump = ["https://cdn.discordapp.com/attachments/834509030110003300/834509475452813349/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509425452253254/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509577025355806/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509462760194108/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509331642712074/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509413934563328/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509549179240458/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509387619237900/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509401423216670/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509436521414756/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509533853515856/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509447429881876/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509592561975296/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509486927773726/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509372553035806/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509345584447518/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509502312480838/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509518033125416/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509359094169621/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509562987413522/jump.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🦘 {ctx.author.mention} **делает прыжок отсюда!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(jump)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="jump", description="Попрыгать")
async def jump (interaction : Interaction, *, text = None):
    jump = ["https://cdn.discordapp.com/attachments/834509030110003300/834509475452813349/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509425452253254/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509577025355806/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509462760194108/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509331642712074/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509413934563328/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509549179240458/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509387619237900/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509401423216670/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509436521414756/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509533853515856/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509447429881876/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509592561975296/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509486927773726/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509372553035806/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509345584447518/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509502312480838/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509518033125416/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509359094169621/jump.gif", "https://cdn.discordapp.com/attachments/834509030110003300/834509562987413522/jump.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🦘 **Ты** делаешь прыжлк отсюда!')
        emb1.set_image(url=f'{random.choice(jump)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def sip (ctx: nextcord.Member, *, text = None):
    sip = ["https://cdn.discordapp.com/attachments/761612990784471041/761613273048678430/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837478748979270/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837495506010152/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613569317666886/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613481614114826/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837435015495720/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/762355934864474112/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613430808510464/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613511892795473/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761620581787238410/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/779071115187978310/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613660744712252/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/1031120861303935116/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/860571962316292096/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/1042439000289452132/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613356704333847/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613393864949760/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837463930503238/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/762358715964850176/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837508943642714/sip.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'☕ {ctx.author.mention} **пьёт горячий чаёк**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(sip)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="sip", description="Пить чай")
async def sip (interaction : Interaction, *, text = None):
    sip = ["https://cdn.discordapp.com/attachments/761612990784471041/761613273048678430/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837478748979270/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837495506010152/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613569317666886/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613481614114826/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837435015495720/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/762355934864474112/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613430808510464/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613511892795473/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761620581787238410/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/779071115187978310/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613660744712252/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/1031120861303935116/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/860571962316292096/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/1042439000289452132/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613356704333847/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/761613393864949760/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837463930503238/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/762358715964850176/sip.gif", "https://cdn.discordapp.com/attachments/761612990784471041/834837508943642714/sip.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'☕ **Ты** пьёшь горячий чаёк')
        emb1.set_image(url=f'{random.choice(sip)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePlay]")
async def yawn (ctx: nextcord.Member, *, text = None):
    yawn = ["https://cdn.discordapp.com/attachments/736262435501113465/736262526651596910/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262631064731668/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262549422604349/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262543294857286/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262480732356618/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/741228041199681546/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262561984544828/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262515029442721/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262595928916048/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262603688640554/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262535459897394/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262557404495872/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262468191649873/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262584621072414/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262590606344242/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262612383301642/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262495081070592/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262569668640838/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262522956414996/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262578526748733/yawn.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🥱 {ctx.author.mention} **зевает**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yawn)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="yawn", description="Зевать")
async def yawn (interaction : Interaction, *, text = None):
    yawn = ["https://cdn.discordapp.com/attachments/736262435501113465/736262526651596910/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262631064731668/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262549422604349/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262543294857286/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262480732356618/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/741228041199681546/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262561984544828/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262515029442721/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262595928916048/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262603688640554/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262535459897394/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262557404495872/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262468191649873/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262584621072414/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262590606344242/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262612383301642/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262495081070592/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262569668640838/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262522956414996/yawn.gif", "https://cdn.discordapp.com/attachments/736262435501113465/736262578526748733/yawn.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🥱 **Вы** зеваете')
        emb1.set_image(url=f'{random.choice(yawn)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def shrug (ctx: nextcord.Member, *, text = None):
    shrug = ["https://cdn.discordapp.com/attachments/743231747415867483/743232043651039283/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232018091081769/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232310358573146/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232278288924752/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232226140880907/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743231795050315787/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232193207205958/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743231970557034597/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232253194141776/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/821077491603079198/shrug.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'¯\_(ツ)_/¯ {ctx.author.mention} **хз**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(shrug)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="shrug", description="Нз")
async def shrug (interaction : Interaction, *, text = None):
    shrug = ["https://cdn.discordapp.com/attachments/743231747415867483/743232043651039283/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232018091081769/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232310358573146/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232278288924752/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232226140880907/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743231795050315787/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232193207205958/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743231970557034597/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/743232253194141776/shrug.gif", "https://cdn.discordapp.com/attachments/743231747415867483/821077491603079198/shrug.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'¯\_(ツ)_/¯ Хз')
        emb1.set_image(url=f'{random.choice(shrug)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def drink (ctx: nextcord.Member, *, text = None):
    drink = ["https://cdn.discordapp.com/attachments/860580103284195358/860584699037745152/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583931501084682/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583818494607390/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860580167989329930/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583666723586058/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584917146796032/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584584902213642/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860585022653071375/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584802670477323/drink.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍻 {ctx.author.mention} **пьёт напиток**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(drink)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="drink", description="Пить напиток")
async def drink (interaction : Interaction, *, text = None):
    drink = ["https://cdn.discordapp.com/attachments/860580103284195358/860584699037745152/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583931501084682/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583818494607390/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860580167989329930/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860583666723586058/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584917146796032/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584584902213642/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860585022653071375/drink.gif", "https://cdn.discordapp.com/attachments/860580103284195358/860584802670477323/drink.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍻 **Ты** пьёшь напиток')
        emb1.set_image(url=f'{random.choice(drink)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def dab (ctx: nextcord.Member, *, text = None):
    dab = ["https://cdn.discordapp.com/attachments/736253507618865215/736253518100299796/dab.gif", "https://cdn.discordapp.com/attachments/736253507618865215/736253511095943269/dab.gif", "https://cdn.discordapp.com/attachments/736253507618865215/736253522198396928/dab.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😎 {ctx.author.mention} **дэббит над хейтерами!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(dab)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="dab", description="Дэббить")
async def dab (interaction : Interaction, *, text = None):
    dab = ["https://cdn.discordapp.com/attachments/736253507618865215/736253518100299796/dab.gif", "https://cdn.discordapp.com/attachments/736253507618865215/736253511095943269/dab.gif", "https://cdn.discordapp.com/attachments/736253507618865215/736253522198396928/dab.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😎 **Ты** дэббишь над хейтерами!')
        emb1.set_image(url=f'{random.choice(dab)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def nom (ctx: nextcord.Member, *, text = None):
    nom = ["https://cdn.discordapp.com/attachments/736273366784278558/736273380373954730/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833799400783882/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273496098865293/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834031115239525/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273452323045466/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833839427026954/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834170072399913/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833770988568637/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833757079994388/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273588960755782/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833810671534080/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834020340334602/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834072848171148/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834107217084476/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834132055490640/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273616211017769/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833901645463552/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834095389409320/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273569201389638/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273567125340250/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833551115288576/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273672775663616/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833981840425021/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273443191914597/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273564315025599/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273489387978792/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834311290159114/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273620275298434/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273472153714719/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834118977519617/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834146375368707/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273405405560892/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273655889133699/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/755840757901820054/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273650537463918/nom.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🌮 {ctx.author.mention} **очень голодный!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(nom)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="nom", description="Хочу кушать")
async def nom (interaction : Interaction, *, text = None):
    nom = ["https://cdn.discordapp.com/attachments/736273366784278558/736273380373954730/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833799400783882/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273496098865293/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834031115239525/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273452323045466/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833839427026954/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834170072399913/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833770988568637/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833757079994388/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273588960755782/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833810671534080/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834020340334602/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834072848171148/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834107217084476/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834132055490640/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273616211017769/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833901645463552/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834095389409320/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273569201389638/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273567125340250/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833551115288576/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273672775663616/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834833981840425021/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273443191914597/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273564315025599/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273489387978792/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834311290159114/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273620275298434/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273472153714719/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834118977519617/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/834834146375368707/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273405405560892/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273655889133699/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/755840757901820054/nom.gif", "https://cdn.discordapp.com/attachments/736273366784278558/736273650537463918/nom.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🌮 **Вы** очень голодны!')
        emb1.set_image(url=f'{random.choice(nom)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def nosebleed (ctx: nextcord.Member, *, text = None):
    nosebleed = ["https://cdn.discordapp.com/attachments/736261590508371980/736261596900491375/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261620728070174/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261644497190962/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261637320736838/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261672938897408/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261667767451768/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261662092558406/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261627740946452/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261602525053009/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261652332281927/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261613270597632/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261646690811965/nosebleed.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🩸 {ctx.author.mention} **идет кровь из носа! >.<**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(nosebleed)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="nosebleed", description=">.<")
async def nosebleed (interaction : Interaction, *, text = None):
    nosebleed = ["https://cdn.discordapp.com/attachments/736261590508371980/736261596900491375/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261620728070174/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261644497190962/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261637320736838/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261672938897408/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261667767451768/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261662092558406/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261627740946452/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261602525053009/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261652332281927/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261613270597632/nosebleed.gif", "https://cdn.discordapp.com/attachments/736261590508371980/736261646690811965/nosebleed.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🩸 У **вас** идет кровь с носа! >.<')
        emb1.set_image(url=f'{random.choice(nosebleed)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def run (ctx: nextcord.Member, *, text = None):
    run = ["https://cdn.discordapp.com/attachments/736259684763435059/736259705567182848/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259890531532810/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259801151045702/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259690962485268/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259884076499074/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259873305526353/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259848282308628/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259792263184515/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259867735621683/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259857266638899/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259959783948358/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259922651512865/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259782364758128/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259723288117369/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259776480149544/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259758641905724/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259953446092921/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259787804639351/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259754514579537/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259694955331694/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259968616890428/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259984127557692/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259715662741504/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259900216311848/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259740811788318/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259702135980144/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259730497994792/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259833338003456/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259744276414534/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259931270807592/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259811766829116/run.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🏃 {ctx.author.mention} **мчится домой!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(run)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="run", description="Бежать")
async def run (interaction : Interaction, *, text = None):
    run = ["https://cdn.discordapp.com/attachments/736259684763435059/736259705567182848/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259890531532810/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259801151045702/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259690962485268/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259884076499074/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259873305526353/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259848282308628/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259792263184515/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259867735621683/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259857266638899/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259959783948358/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259922651512865/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259782364758128/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259723288117369/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259776480149544/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259758641905724/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259953446092921/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259787804639351/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259754514579537/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259694955331694/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259968616890428/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259984127557692/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259715662741504/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259900216311848/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259740811788318/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259702135980144/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259730497994792/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259833338003456/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259744276414534/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259931270807592/run.gif", "https://cdn.discordapp.com/attachments/736259684763435059/736259811766829116/run.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🏃‍♂️ **Ты** мчишься домой!')
        emb1.set_image(url=f'{random.choice(run)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def sleep (ctx: nextcord.Member, *, text = None):
    sleep = ["https://cdn.discordapp.com/attachments/736261025166524498/736261183094521856/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261105264885770/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925456007658881044/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455784698085426/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838551332913172/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838307082862613/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261278250565662/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261058494333008/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838375834976327/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261089083392020/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/881899944871592026/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838157203603496/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261150777540708/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838704639967282/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/881899546731479140/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838231144988742/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455660584411146/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838389484027964/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838472006696960/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838537467461662/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838334265491466/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838320945037342/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838361859686471/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261044783153222/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838622884462642/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261270105358396/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261314514780230/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455887475290172/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261283615342672/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261070666203158/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838092778176512/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838647203299429/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838167886626846/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838281291038780/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261165151420486/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261078563946618/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838669801816184/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261138173526076/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838413634306078/sleep.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😴 {ctx.author.mention} **споки ноки!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(sleep)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="sleep", description="Спатки")
async def sleep (interaction : Interaction, *, text = None):
    sleep = ["https://cdn.discordapp.com/attachments/736261025166524498/736261183094521856/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261105264885770/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925456007658881044/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455784698085426/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838551332913172/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838307082862613/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261278250565662/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261058494333008/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838375834976327/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261089083392020/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/881899944871592026/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838157203603496/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261150777540708/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838704639967282/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/881899546731479140/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838231144988742/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455660584411146/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838389484027964/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838472006696960/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838537467461662/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838334265491466/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838320945037342/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838361859686471/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261044783153222/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838622884462642/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261270105358396/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261314514780230/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/925455887475290172/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261283615342672/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261070666203158/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838092778176512/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838647203299429/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838167886626846/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838281291038780/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261165151420486/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261078563946618/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838669801816184/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/736261138173526076/sleep.gif", "https://cdn.discordapp.com/attachments/736261025166524498/834838413634306078/sleep.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😴 споки ноки **тебе**!')
        emb1.set_image(url=f'{random.choice(sleep)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def stare (ctx: nextcord.Member, *, text = None):
    stare = ["https://cdn.discordapp.com/attachments/736260687633842216/834842817250852884/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843445624569956/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834842954874748948/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843239940620308/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843430449315901/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260901484625950/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843020129468476/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834842771629146122/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260936528166963/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260822317137940/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260884573323394/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260742839271424/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260905527934986/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843155659751515/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260805212766288/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843366747144192/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260731065991278/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843109099438170/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843060931264522/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260921600508005/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260765467672756/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260786942509076/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843227865612358/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260702947508244/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843416515838032/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843460611604500/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843097237422080/stare.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👀 {ctx.author.mention} **видит всё!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(stare)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="stare", description="Всевидищий")
async def stare (interaction : Interaction, *, text = None):
    stare = ["https://cdn.discordapp.com/attachments/736260687633842216/834842817250852884/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843445624569956/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834842954874748948/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843239940620308/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843430449315901/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260901484625950/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843020129468476/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834842771629146122/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260936528166963/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260822317137940/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260884573323394/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260742839271424/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260905527934986/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843155659751515/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260805212766288/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843366747144192/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260731065991278/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843109099438170/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843060931264522/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260921600508005/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260765467672756/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260786942509076/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843227865612358/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/736260702947508244/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843416515838032/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843460611604500/stare.gif", "https://cdn.discordapp.com/attachments/736260687633842216/834843097237422080/stare.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👀 **Вы** видите всё!')
        emb1.set_image(url=f'{random.choice(stare)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def laugh (ctx: nextcord.Member, *, text = None):
    laugh = ["https://cdn.discordapp.com/attachments/736261908960903268/736262065659969586/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261919228297256/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262151227965477/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262112862666873/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262227014713476/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261998060372110/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262133586591875/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512083491225680/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262047733514260/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512306444173322/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262118155747370/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262326545547284/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512170825023578/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262053068669009/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/881898218953252894/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512120082333728/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261929936617522/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512262147604510/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512277126250567/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262024958574613/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262004003700876/laugh.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😂 {ctx.author.mention} **думает что это весело!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(laugh)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="laugh", description="Весело")
async def laugh (interaction : Interaction, *, text = None):
    laugh = ["https://cdn.discordapp.com/attachments/736261908960903268/736262065659969586/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261919228297256/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262151227965477/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262112862666873/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262227014713476/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261998060372110/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262133586591875/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512083491225680/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262047733514260/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512306444173322/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262118155747370/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262326545547284/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512170825023578/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262053068669009/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/881898218953252894/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512120082333728/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736261929936617522/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512262147604510/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/834512277126250567/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262024958574613/laugh.gif", "https://cdn.discordapp.com/attachments/736261908960903268/736262004003700876/laugh.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤣 **Ты** думаешь что это весело!')
        emb1.set_image(url=f'{random.choice(laugh)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePlay]")
async def yaoicuddle (ctx, member : nextcord.Member, *, text = None):
    yaoicuddle = ["https://cdn.discordapp.com/attachments/736279874452455454/736279927313268786/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279896518557787/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279911534428271/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279946741153882/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279883776262144/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/912101389449166868/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/912101261183160351/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279917976617020/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279903036506202/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279930203013270/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279914172645556/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279906564178000/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279889224925214/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279935152554044/yaoicuddle.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨👐👨 {ctx.author.mention} **прижимается к** {member.mention} **в стиле яой!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yaoicuddle)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👨👐👨 {ctx.author.mention} **прижимается к** {member.mention} **в стиле яой!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yaoicuddle)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yaoicuddle", description="Прижиматься в стиле яой к пользователю")
async def yaoicuddle (interaction : Interaction, member : nextcord.Member, *, text = None):
    yaoicuddle = ["https://cdn.discordapp.com/attachments/736279874452455454/736279927313268786/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279896518557787/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279911534428271/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279946741153882/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279883776262144/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/912101389449166868/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/912101261183160351/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279917976617020/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279903036506202/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279930203013270/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279914172645556/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279906564178000/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279889224925214/yaoicuddle.gif", "https://cdn.discordapp.com/attachments/736279874452455454/736279935152554044/yaoicuddle.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨👐👨 **Ты** **прижимаешься к** {member.mention} **в стиле яой!**')
        emb1.set_image(url=f'{random.choice(yaoicuddle)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👨👐👨 **Ты** **прижимаешься к** {member.mention} **в стиле яой!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yaoicuddle)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def yaoihug (ctx, member : nextcord.Member, *, text = None):
    yaoihug = ["https://cdn.discordapp.com/attachments/736278340733894710/741227684587241503/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278379849973780/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278358869934101/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278410568925315/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278403434676224/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278350959607949/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278344986918954/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278366818271302/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278374993100840/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278355015630868/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278429510533176/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/881896699277238282/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278434866790532/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/834717466424901652/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/877645631051665519/yaoihug.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨👐👨 {ctx.author.mention} **обнимает** {member.mention} **в стиле яой!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yaoihug)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👨👐👨 {ctx.author.mention} **обнимает** {member.mention} **в стиле яой!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yaoihug)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yaoihug", description="обнимать в стиле яой к пользователя")
async def yaoihug (interaction : Interaction, member : nextcord.Member, *, text = None):
    yaoihug = ["https://cdn.discordapp.com/attachments/736278340733894710/741227684587241503/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278379849973780/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278358869934101/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278410568925315/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278403434676224/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278350959607949/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278344986918954/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278366818271302/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278374993100840/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278355015630868/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278429510533176/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/881896699277238282/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/736278434866790532/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/834717466424901652/yaoihug.gif", "https://cdn.discordapp.com/attachments/736278340733894710/877645631051665519/yaoihug.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨👐👨 **Ты** **обнимаешь** {member.mention} **в стиле яой!**')
        emb1.set_image(url=f'{random.choice(yaoihug)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👨👐👨 **Ты** **обнимаешь** {member.mention} **в стиле яой!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yaoihug)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def yuricuddle (ctx, member : nextcord.Member, *, text = None):
    yuricuddle = ["https://cdn.discordapp.com/attachments/736280073379774536/834849079427203112/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280178623250568/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280113208885268/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280093290135622/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/829471458212052992/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280078975238154/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280085903966339/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280083110690836/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280076546474075/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280099342778498/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280110692565062/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/834849068630671450/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280106825416785/yuricuddle.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩👐👩 {ctx.author.mention} **прижимается к** {member.mention} **в стиле юри!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yuricuddle)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👩👐👩 {ctx.author.mention} **прижимается к** {member.mention} **в стиле юри!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yuricuddle)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yuricuddle", description="Прижиматься в стиле юри к пользователю")
async def yuricuddle (interaction : Interaction, member : nextcord.Member, *, text = None):
    yuricuddle = ["https://cdn.discordapp.com/attachments/736280073379774536/834849079427203112/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280178623250568/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280113208885268/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280093290135622/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/829471458212052992/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280078975238154/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280085903966339/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280083110690836/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280076546474075/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280099342778498/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280110692565062/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/834849068630671450/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280106825416785/yuricuddle.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩👐👩 **Ты** **прижимаешься к** {member.mention} **в стиле юри!**')
        emb1.set_image(url=f'{random.choice(yuricuddle)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👩👐👩 **Ты** **прижимаешься к** {member.mention} **в стиле юри!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yuricuddle)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def yurihug (ctx, member : nextcord.Member, *, text = None):
    yurihug = ["https://cdn.discordapp.com/attachments/736280073379774536/834849079427203112/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280178623250568/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280113208885268/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280093290135622/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/829471458212052992/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280078975238154/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280085903966339/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280083110690836/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280076546474075/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280099342778498/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280110692565062/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/834849068630671450/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280106825416785/yuricuddle.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩👐👩 {ctx.author.mention} **обнимает** {member.mention} **в стиле юри!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yurihug)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👩👐👩 {ctx.author.mention} **обнимает** {member.mention} **в стиле юри!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yurihug)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yurihug", description="Обнимать в стиле юри пользователя")
async def yurihug (interaction : Interaction, member : nextcord.Member, *, text = None):
    yurihug = ["https://cdn.discordapp.com/attachments/736280073379774536/834849079427203112/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280178623250568/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280113208885268/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280093290135622/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/829471458212052992/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280078975238154/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280085903966339/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280083110690836/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280076546474075/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280099342778498/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280110692565062/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/834849068630671450/yuricuddle.gif", "https://cdn.discordapp.com/attachments/736280073379774536/736280106825416785/yuricuddle.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩👐👩 **Ты** **обнимаешь** {member.mention} **в стиле юри!**')
        emb1.set_image(url=f'{random.choice(yurihug)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👩👐👩 **Ты** **обнимаешь** {member.mention} **в стиле юри!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yurihug)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def yaoikiss (ctx, member : nextcord.Member, *, text = None):
    yaoikiss = ["https://cdn.discordapp.com/attachments/736280745601007737/736280845991542824/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/834852296596783154/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/991345678464856094/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280917433253928/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280822331473930/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280860105506816/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280786956976168/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280839658143805/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280757068234823/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/845981040148348998/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280925477928960/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/783755433126264912/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/774620635997011978/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280806497976360/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736284502275522670/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280753842683994/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/783699292757164102/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280871895695480/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/912100600999723018/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736284287359254599/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280812973981786/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280826047889448/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280852501233674/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280803624878210/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280751187689482/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280880162537472/yaoikiss.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨‍❤️‍👨 {ctx.author.mention} **целует** {member.mention} **в стиле яой!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yaoikiss)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👨‍❤️‍👨 {ctx.author.mention} **целует** {member.mention} **в стиле яой!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yaoikiss)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yaoikiss", description="Целовать в стиле яой пользователя")
async def yaoikiss (interaction : Interaction, member : nextcord.Member, *, text = None):
    yaoikiss = ["https://cdn.discordapp.com/attachments/736280745601007737/736280845991542824/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/834852296596783154/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/991345678464856094/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280917433253928/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280822331473930/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280860105506816/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280786956976168/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280839658143805/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280757068234823/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/845981040148348998/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280925477928960/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/783755433126264912/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/774620635997011978/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280806497976360/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736284502275522670/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280753842683994/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/783699292757164102/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280871895695480/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/912100600999723018/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736284287359254599/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280812973981786/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280826047889448/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280852501233674/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280803624878210/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280751187689482/yaoikiss.gif", "https://cdn.discordapp.com/attachments/736280745601007737/736280880162537472/yaoikiss.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨‍❤️‍👨 **Ты** **целуешь** {member.mention} **в стиле яой!**')
        emb1.set_image(url=f'{random.choice(yaoikiss)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👨‍❤️‍👨 **Ты** **целуешь** {member.mention} **в стиле яой!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yaoikiss)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def yeet (ctx, member : nextcord.Member, *, text = None):
    yeet = ["https://cdn.discordapp.com/attachments/910944832845905980/910945626911555644/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945848337236008/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945162706968596/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945255141023755/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945707337322567/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910946009486614528/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945933691338772/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945543176454214/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945462650040430/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945354596364308/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945626911555644/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945848337236008/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945162706968596/yeet.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💨 {ctx.author.mention} **швырнул** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yeet)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💨 {ctx.author.mention} **швырнул** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yeet)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yeet", description="Швырнуть пользователя")
async def yeet (interaction : Interaction, member : nextcord.Member, *, text = None):
    yeet = ["https://cdn.discordapp.com/attachments/910944832845905980/910945626911555644/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945848337236008/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945162706968596/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945255141023755/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945707337322567/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910946009486614528/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945933691338772/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945543176454214/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945462650040430/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945354596364308/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945626911555644/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945848337236008/yeet.gif", "https://cdn.discordapp.com/attachments/910944832845905980/910945162706968596/yeet.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💨 **Ты** **швырнул** {member.mention}**')
        emb1.set_image(url=f'{random.choice(yeet)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'💨 **Ты** **швырнул** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yeet)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def highfive (ctx, member : nextcord.Member, *, text = None):
    highfive = ["https://cdn.discordapp.com/attachments/736274901673181216/834508169634906142/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275023697936425/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508208038608906/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274948129030144/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508220034711552/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275088323903558/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275017297428511/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274922028138606/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275073866006568/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/881895480227938334/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274926260060251/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508141907279932/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508183355129856/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275014097305660/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275096833884261/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508196030316654/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275028873576478/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274943276220416/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275069109796894/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275057722130462/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274955003494410/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275063833100288/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274994304122960/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274966286172225/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274978973941891/highfive.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤚 {ctx.author.mention} **дай пятюню!** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(highfive)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🤚 {ctx.author.mention} **дай пятюню!** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(highfive)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="highfive", description="Дай пять!")
async def highfive (interaction : Interaction, member : nextcord.Member, *, text = None):
    highfive = ["https://cdn.discordapp.com/attachments/736274901673181216/834508169634906142/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275023697936425/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508208038608906/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274948129030144/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508220034711552/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275088323903558/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275017297428511/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274922028138606/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275073866006568/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/881895480227938334/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274926260060251/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508141907279932/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508183355129856/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275014097305660/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275096833884261/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/834508196030316654/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275028873576478/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274943276220416/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275069109796894/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275057722130462/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274955003494410/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736275063833100288/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274994304122960/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274966286172225/highfive.gif", "https://cdn.discordapp.com/attachments/736274901673181216/736274978973941891/highfive.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🤚 **Ты** **даешь пятюню!** {member.mention}')
        emb1.set_image(url=f'{random.choice(highfive)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🤚 **Ты** **даешь пятюню** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(highfive)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def massage (ctx, member : nextcord.Member, *, text = None):
    massage = ["https://cdn.discordapp.com/attachments/736276388226662420/736276410762526752/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276423819526174/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276394828627968/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276400524492950/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276427174969354/massage.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💆 {ctx.author.mention} **делает массаж!** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(massage)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💆 {ctx.author.mention} **делает массаж!** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(massage)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="massage", description="Сделать массаж")
async def massage (interaction : Interaction, member : nextcord.Member, *, text = None):
    massage = ["https://cdn.discordapp.com/attachments/736276388226662420/736276410762526752/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276423819526174/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276394828627968/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276400524492950/massage.gif", "https://cdn.discordapp.com/attachments/736276388226662420/736276427174969354/massage.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💆 **Ты** **делаешь массаж!** {member.mention}')
        emb1.set_image(url=f'{random.choice(massage)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'💆 **Ты** **делаешь массаж!** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(massage)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def marry (ctx, member : nextcord.Member, *, text = None):
    marry = ["https://cdn.discordapp.com/attachments/736281363464060979/736281396355530812/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281399065051137/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281376898154546/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281381692244048/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281405088202782/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281372750118912/marry.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💍 {ctx.author.mention} **и** {member.mention} **поженились! Как мило! >-<**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(marry)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💍 {ctx.author.mention} **и** {member.mention} **поженились! Как мило! >-<**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(marry)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="marry", description="Поженить")
async def marry (interaction : Interaction, member : nextcord.Member, *, text = None):
    marry = ["https://cdn.discordapp.com/attachments/736281363464060979/736281396355530812/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281399065051137/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281376898154546/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281381692244048/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281405088202782/marry.gif", "https://cdn.discordapp.com/attachments/736281363464060979/736281372750118912/marry.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💍 **Ты** **и** {member.mention} **поженились! Как мило! >-<**')
        emb1.set_image(url=f'{random.choice(marry)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'💍 **Ты** **и** {member.mention} **поженились! Как мило! >-<**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(marry)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def merkel (ctx, member : nextcord.Member, *, text = None):
    merkel = ["https://cdn.discordapp.com/attachments/736269653948760146/736269660143747082/merkel.png"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🇩🇪 {ctx.author.mention} **меркельнул** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(merkel)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🇩🇪 {ctx.author.mention} **меркельнул** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(merkel)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="merkel", description="Меркельнуть")
async def merkel (interaction : Interaction, member : nextcord.Member, *, text = None):
    merkel = ["https://cdn.discordapp.com/attachments/736269653948760146/736269660143747082/merkel.png"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🇩🇪 **Ты** **меркельнул** {member.mention}')
        emb1.set_image(url=f'{random.choice(merkel)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🇩🇪 **Ты** **меркельнул** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(merkel)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def reward (ctx: nextcord.Member, *, text = None):
    reward = ["https://cdn.discordapp.com/attachments/736276242466078761/893968043774996490/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569245600153660/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568281279336448/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569140675452958/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569328454455346/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893968111945023588/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967786341203968/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568422241529946/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569060773961880/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/736276249969950781/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568778174361610/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967575573200906/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568536582422588/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967971326763059/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568918062788678/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967877269504040/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/991341412861874246/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568693650743376/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967683048059021/reward.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍓 {ctx.author.mention} **Вы сделали что-то великое! В награду, я даю тебе эту клубнику!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(reward)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="reward", description="Подарок")
async def reward (interaction : Interaction, *, text = None):
    reward = ["https://cdn.discordapp.com/attachments/736276242466078761/893968043774996490/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569245600153660/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568281279336448/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569140675452958/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569328454455346/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893968111945023588/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967786341203968/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568422241529946/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885569060773961880/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/736276249969950781/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568778174361610/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967575573200906/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568536582422588/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967971326763059/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568918062788678/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967877269504040/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/991341412861874246/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/885568693650743376/reward.gif", "https://cdn.discordapp.com/attachments/736276242466078761/893967683048059021/reward.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍓 **Вы** Вы сделали что-то великое! В награду, я даю тебе эту клубнику!!')
        emb1.set_image(url=f'{random.choice(reward)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def squish (ctx, member : nextcord.Member, *, text = None):
    squish = ["https://cdn.discordapp.com/attachments/955386888624148491/955387215511433226/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387363712974848/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387497041502208/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387528523944006/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387234524213299/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387465257082890/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387410596892752/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387024976793640/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387385502400522/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387385502400522/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387448026873876/squish.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍩 {ctx.author.mention} **тискает** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(squish)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍩 {ctx.author.mention} **тискает** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(squish)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="squish", description="Тискать пользователя")
async def squish (interaction : Interaction, member : nextcord.Member, *, text = None):
    squish = ["https://cdn.discordapp.com/attachments/955386888624148491/955387215511433226/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387363712974848/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387497041502208/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387528523944006/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387234524213299/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387465257082890/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387410596892752/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387024976793640/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387385502400522/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387385502400522/squish.gif", "https://cdn.discordapp.com/attachments/955386888624148491/955387448026873876/squish.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍩 **Вы** **тискаете** {member.mention}')
        emb1.set_image(url=f'{random.choice(squish)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍩 **Вы** **тискаете** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(squish)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def bonk (ctx, member : nextcord.Member, *, text = None):
    bonk = ["https://cdn.discordapp.com/attachments/826095943748943913/826095979614044180/bonk.gif", "https://media.tenor.com/TbLpG9NCzjkAAAAC/bonk.gif", "https://media.tenor.com/5YrUft9OXfUAAAAC/bonk-doge.gif", "https://thumbs.gfycat.com/TediousNaturalAffenpinscher-size_restricted.gif", "https://media.tenor.com/636jxoYmHfgAAAAd/bonk-ultimate-bonk.gif", "https://i.pinimg.com/originals/b0/d2/70/b0d270b7c07757cc6c3fb6efc60229e8.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🏏 {ctx.author.mention} **посадил** {member.mention} **в секс-тюрьму!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(bonk)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🏏 {ctx.author.mention} **посадил** {member.mention} **в секс-тюрьму!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(bonk)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="bonk", description="Посадить пользователя")
async def bonk (interaction : Interaction, member : nextcord.Member, *, text = None):
    bonk = ["https://cdn.discordapp.com/attachments/826095943748943913/826095979614044180/bonk.gif", "https://media.tenor.com/TbLpG9NCzjkAAAAC/bonk.gif", "https://media.tenor.com/5YrUft9OXfUAAAAC/bonk-doge.gif", "https://thumbs.gfycat.com/TediousNaturalAffenpinscher-size_restricted.gif", "https://media.tenor.com/636jxoYmHfgAAAAd/bonk-ultimate-bonk.gif", "https://i.pinimg.com/originals/b0/d2/70/b0d270b7c07757cc6c3fb6efc60229e8.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🏏 **Ты** **посадил** {member.mention} **в секс-тюрьму!**')
        emb1.set_image(url=f'{random.choice(bonk)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🏏 **Ты** **посадил** {member.mention} **в секс-тюрьму!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(bonk)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def yurikiss (ctx, member : nextcord.Member, *, text = None):
    yurikiss = ["https://cdn.discordapp.com/attachments/736281091534618674/736281124774346822/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/925455445311782973/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/863573727069077545/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281133649756273/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849805246660608/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281183738003456/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281204617248848/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281104201285732/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849818278887435/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/892166330340499506/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281161139093544/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849792659947520/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849832022704158/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281140683604080/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281151748047088/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281096764784780/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281115098087506/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281165736181860/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281173185265794/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849779824853023/yurikiss.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩‍❤️‍👩 {ctx.author.mention} **целует** {member.mention} **в стиле юри!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yurikiss)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👩‍❤️‍👩 {ctx.author.mention} **целует** {member.mention} **в стиле юри!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yurikiss)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="yurikiss", description="Поцеловать пользователя в стиле юри")
async def yurikiss (interaction : Interaction, member : nextcord.Member, *, text = None):
    yurikiss = ["https://cdn.discordapp.com/attachments/736281091534618674/736281124774346822/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/925455445311782973/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/863573727069077545/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281133649756273/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849805246660608/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281183738003456/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281204617248848/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281104201285732/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849818278887435/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/892166330340499506/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281161139093544/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849792659947520/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849832022704158/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281140683604080/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281151748047088/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281096764784780/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281115098087506/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281165736181860/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/736281173185265794/yurikiss.gif", "https://cdn.discordapp.com/attachments/736281091534618674/834849779824853023/yurikiss.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩‍❤️‍👩 **Вы** **целуете** {member.mention} **в стиле юри!**')
        emb1.set_image(url=f'{random.choice(yurikiss)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👩‍❤️‍👩 **Вы** **целуете** {member.mention} **в стиле юри!**\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(yurikiss)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def arrest (ctx, member : nextcord.Member, *, text = None):
    arrest = ["https://cdn.discordapp.com/attachments/992095513073700994/992095956130607295/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096227699216425/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095641901744198/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095593394622475/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095783438520361/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096151895556217/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095681474986025/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096182409109675/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096116868915321/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095919736619128/arrest.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👮 {ctx.author.mention} **арестовал** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(arrest)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👮 {ctx.author.mention} **арестовал** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(arrest)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="arrest", description="Арестовать пользователя")
async def arrest (interaction : Interaction, member : nextcord.Member, *, text = None):
    arrest = ["https://cdn.discordapp.com/attachments/992095513073700994/992095956130607295/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096227699216425/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095641901744198/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095593394622475/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095783438520361/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096151895556217/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095681474986025/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096182409109675/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992096116868915321/arrest.gif", "https://cdn.discordapp.com/attachments/992095513073700994/992095919736619128/arrest.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👮‍♂️ **Ты** **арестовал** {member.mention}')
        emb1.set_image(url=f'{random.choice(arrest)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👮‍♂️ **Ты** **арестовал** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(arrest)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def awkward (ctx: nextcord.Member, *, text = None):
    awkward = ["https://cdn.discordapp.com/attachments/736253855339249695/736253931860000879/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253935895183430/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253952143655032/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253947248902254/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253858308817007/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253927963492512/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253958380585080/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253895185268797/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253865015377960/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253920858603580/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253872057745539/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253876914880542/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253900210044929/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253908279623731/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253915129053184/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253940957577226/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253887203377172/awkward.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😅 {ctx.author.mention} **чувствует себя неловко UwU**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(awkward)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="awkward", description="UwU")
async def awkward (interaction : Interaction, *, text = None):
    awkward = ["https://cdn.discordapp.com/attachments/736253855339249695/736253931860000879/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253935895183430/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253952143655032/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253947248902254/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253858308817007/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253927963492512/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253958380585080/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253895185268797/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253865015377960/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253920858603580/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253872057745539/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253876914880542/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253900210044929/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253908279623731/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253915129053184/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253940957577226/awkward.gif", "https://cdn.discordapp.com/attachments/736253855339249695/736253887203377172/awkward.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'😅 **Ты** чувствуешь себя не ловко UwU')
        emb1.set_image(url=f'{random.choice(awkward)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[RolePLay]")
async def ghoul (ctx: nextcord.Member, *, text = None):
    ghoul = ["https://media.tenor.com/cZfEvBW200EAAAAC/%D0%B3%D1%83%D0%BB%D1%8C-%D1%82%D0%BE%D0%BA%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://media.tenor.com/obZNRpreIsQAAAAM/laborat%C3%B3rio-de-trava.gif", "https://i.pinimg.com/originals/23/c6/e4/23c6e442815b36ae61fa8e046b8dcdc5.gif", "https://media.tenor.com/QimBFNmAE1YAAAAC/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://media.tenor.com/MtvAD5FVpMEAAAAC/tokyo-ghoul-tg.gif", "https://i.gifer.com/8XBA.gif", "https://i.pinimg.com/originals/cf/7f/b9/cf7fb933b954a8514c545417b2966701.gif", "https://static.wikia.nocookie.net/tokyoghoul/images/c/cf/Kaneki%27s_kakugan.gif/revision/latest?cb=20151225111231&path-prefix=ru", "https://media.tenor.com/KbQpqEkQUJ0AAAAC/%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://otkritkis.com/wp-content/uploads/2022/06/qffoz.gif", "https://i.pinimg.com/originals/63/e0/c9/63e0c96983d00738158d4464931af111.gif", "https://i.gifer.com/origin/16/1643e2dc4a2e0463a158353d95b9ccee_w200.gif", "https://otkritkis.com/wp-content/uploads/2022/06/karov.gif", "https://i.gifer.com/origin/a6/a6aa6d12e10fda0650ffd5c9988f9a33_w200.gif", "https://thumbs.gfycat.com/NimbleFatalEquine-max-1mb.gif", "https://media.tenor.com/Vk99BwgU9BIAAAAM/tokyo-ghoul.gif", "https://media.tenor.com/sowwI_isl80AAAAd/%D0%B3%D1%83%D0%BB%D1%8C-%D0%B4%D0%B5%D0%B4%D0%B8%D0%BD%D1%81%D0%B0%D0%B9%D0%B4.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👻 {ctx.author.mention} **превратился в гуля**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(ghoul)}')
        await ctx.send(embed=emb1)

@bot.slash_command(name="ghoul", description="Стать дед инсайдом")
async def ghoul (interaction : Interaction, *, text = None):
    ghoul = ["https://media.tenor.com/cZfEvBW200EAAAAC/%D0%B3%D1%83%D0%BB%D1%8C-%D1%82%D0%BE%D0%BA%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://media.tenor.com/obZNRpreIsQAAAAM/laborat%C3%B3rio-de-trava.gif", "https://i.pinimg.com/originals/23/c6/e4/23c6e442815b36ae61fa8e046b8dcdc5.gif", "https://media.tenor.com/QimBFNmAE1YAAAAC/%D0%B1%D0%B5%D0%B1%D1%80%D0%B0-%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://media.tenor.com/MtvAD5FVpMEAAAAC/tokyo-ghoul-tg.gif", "https://i.gifer.com/8XBA.gif", "https://i.pinimg.com/originals/cf/7f/b9/cf7fb933b954a8514c545417b2966701.gif", "https://static.wikia.nocookie.net/tokyoghoul/images/c/cf/Kaneki%27s_kakugan.gif/revision/latest?cb=20151225111231&path-prefix=ru", "https://media.tenor.com/KbQpqEkQUJ0AAAAC/%D0%B3%D1%83%D0%BB%D1%8C.gif", "https://otkritkis.com/wp-content/uploads/2022/06/qffoz.gif", "https://i.pinimg.com/originals/63/e0/c9/63e0c96983d00738158d4464931af111.gif", "https://i.gifer.com/origin/16/1643e2dc4a2e0463a158353d95b9ccee_w200.gif", "https://otkritkis.com/wp-content/uploads/2022/06/karov.gif", "https://i.gifer.com/origin/a6/a6aa6d12e10fda0650ffd5c9988f9a33_w200.gif", "https://thumbs.gfycat.com/NimbleFatalEquine-max-1mb.gif", "https://media.tenor.com/Vk99BwgU9BIAAAAM/tokyo-ghoul.gif", "https://media.tenor.com/sowwI_isl80AAAAd/%D0%B3%D1%83%D0%BB%D1%8C-%D0%B4%D0%B5%D0%B4%D0%B8%D0%BD%D1%81%D0%B0%D0%B9%D0%B4.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👻 **Ты** превратился в гуля')
        emb1.set_image(url=f'{random.choice(ghoul)}')
        await (interaction.response.send_message(embed=emb1))

@bot.command(usage="[пользователь]")
async def avatar(ctx, *, user: nextcord.Member):
    await ctx.send(user.display_avatar)

@bot.slash_command(name="avatar", description="Посмотреть аватраку пользователя")
async def avatar(ctx, *, user: nextcord.Member):
    await ctx.send(user.display_avatar)

@bot.command(name="banner")
async def server_banner(ctx, member: nextcord.Member):
    try:
        user = await bot.fetch_user(member.id)
        banner_url = user.banner.url
        emb = nextcord.Embed(color=0x2F3136)
        emb.set_image(url=banner_url)
        await ctx.send(content=f"Баннер **{member.name}**", embed=emb)
    except Exception:
        await ctx.send("У указаного пользователя нет баннера!")

@bot.slash_command(name="banner", description="Посмотреть баннер пользователя")
async def banner(ctx, member: nextcord.Member):
    try:
        user = await bot.fetch_user(member.id)
        banner_url = user.banner.url
        emb = nextcord.Embed(color=0x2F3136)
        emb.set_image(url=banner_url)
        await ctx.send(content=f"Баннер **{member.name}**", embed=emb)
    except Exception:
        await ctx.send("У указаного пользователя нет баннера!")

@bot.command(usage="[RolePLay]")
async def sixnine (ctx, member : nextcord.Member, *, text = None):
    sixnine = ["https://cdn.discordapp.com/attachments/969973669126340758/969974394178928660/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974427569762314/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974368648175706/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974239987892304/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974337576796180/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974274003714068/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973746679046154/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974210329997363/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974301258293268/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973986052153364/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974394178928660/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974337576796180/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973746679046154/69.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👅💦 {ctx.author.mention} **делает 69 вместе с** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(sixnine)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👅💦 {ctx.author.mention} **делает 69 вместе с** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(sixnine)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="sixnine", description="Делать 69 вместе с пользователем")
async def sixnine (interaction : Interaction, member : nextcord.Member, *, text = None):
    sixnine = ["https://cdn.discordapp.com/attachments/969973669126340758/969974394178928660/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974427569762314/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974368648175706/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974239987892304/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974337576796180/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974274003714068/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973746679046154/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974210329997363/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974301258293268/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973986052153364/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974394178928660/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969974337576796180/69.gif", "https://cdn.discordapp.com/attachments/969973669126340758/969973746679046154/69.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👅💦 **Ты** **делаешь 69 вместе с** {member.mention}')
        emb1.set_image(url=f'{random.choice(sixnine)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'👅💦 **Ты** **делаешь 69 вместе с** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(sixnine)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def assfuck (ctx, member : nextcord.Member, *, text = None):
    assfuck = ["https://cdn.discordapp.com/attachments/965979549533872319/965979877922717746/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979902828511272/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979631041789993/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979800223227984/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965981047575699476/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965980358581563402/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979778542878750/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979846381559838/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979664352968714/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965980336204939294/assfuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆🍑 {ctx.author.mention} **трахает в попу** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(assfuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆🍑 {ctx.author.mention} **трахает в попу** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(assfuck)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="assfuck", description="Трахать пользователя в попу")
async def assfuck (interaction : Interaction, member : nextcord.Member, *, text = None):
    assfuck = ["https://cdn.discordapp.com/attachments/965979549533872319/965979877922717746/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979902828511272/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979631041789993/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979800223227984/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965981047575699476/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965980358581563402/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979778542878750/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979846381559838/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965979664352968714/assfuck.gif", "https://cdn.discordapp.com/attachments/965979549533872319/965980336204939294/assfuck.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆🍑 **Ты** **трахаешь в попу** {member.mention}')
        emb1.set_image(url=f'{random.choice(assfuck)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍆🍑 **Ты** **трахаешь в попу** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(assfuck)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def assgrab (ctx, member : nextcord.Member, *, text = None):
    assgrab = ["https://cdn.discordapp.com/attachments/834460432818241566/834462015236997191/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462042706542643/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461989321441300/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461948993208340/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462003274711077/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461976402460732/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461961277931610/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462028906233866/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/881905588206968832/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461925894127651/assgrab.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍑👐 {ctx.author.mention} **лапает попку у** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(assgrab)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍑👐 {ctx.author.mention} **лапает попку у** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(assgrab)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="assgrab", description="Лапать попочу у пользователя")
async def assgrab (interaction : Interaction, member : nextcord.Member, *, text = None):
    assgrab = ["https://cdn.discordapp.com/attachments/834460432818241566/834462015236997191/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462042706542643/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461989321441300/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461948993208340/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462003274711077/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461976402460732/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461961277931610/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834462028906233866/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/881905588206968832/assgrab.gif", "https://cdn.discordapp.com/attachments/834460432818241566/834461925894127651/assgrab.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍑👐 **Ты** **лапаешь попку у** {member.mention}')
        emb1.set_image(url=f'{random.choice(assgrab)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍑👐 **Ты** **лапаешь попку у** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(assgrab)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def blowjob (ctx, member : nextcord.Member, *, text = None):
    blowjob = ["https://cdn.discordapp.com/attachments/834490895260844032/834491311238283315/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904674318471258/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491298353381446/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491339138924574/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491273691136041/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904551949635604/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491235456516156/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491115314610277/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491323016806531/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491215537242182/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491350865936434/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904859471818862/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491248382705684/blowjob.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆💦 {ctx.author.mention} **сделал минет** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(blowjob)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆💦 {ctx.author.mention} **сделал минет** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(blowjob)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="blowjob", description="Сделать минет пользователю")
async def blowjob (interaction : Interaction, member : nextcord.Member, *, text = None):
    blowjob = ["https://cdn.discordapp.com/attachments/834490895260844032/834491311238283315/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904674318471258/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491298353381446/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491339138924574/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491273691136041/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904551949635604/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491235456516156/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491115314610277/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491323016806531/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491215537242182/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491350865936434/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/881904859471818862/blowjob.gif", "https://cdn.discordapp.com/attachments/834490895260844032/834491248382705684/blowjob.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆💦 **Ты** **делаешь минет** {member.mention}')
        emb1.set_image(url=f'{random.choice(blowjob)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍆💦 **Ты** **делаешь минет** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(blowjob)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def bondage (ctx, member : nextcord.Member, *, text = None):
    bondage = ["https://cdn.discordapp.com/attachments/992100317430808596/992100561044373504/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102896101503057/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102611161452627/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102066786934914/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102158830927932/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102732100010094/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992101812880551986/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102275608752288/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102396731859064/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100428948979812/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100598008791151/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100531730399232/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102941173485639/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100462910251138/bondage.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🪢 {ctx.author.mention} **занимается развратными бондажными штучками вместе с** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(bondage)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🪢 {ctx.author.mention} **занимается развратными бондажными штучками вместе с** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(bondage)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="bondage", description="Секс игрушки")
async def bondage (interaction : Interaction, member : nextcord.Member, *, text = None):
    bondage = ["https://cdn.discordapp.com/attachments/992100317430808596/992100561044373504/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102896101503057/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102611161452627/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102066786934914/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102158830927932/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102732100010094/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992101812880551986/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102275608752288/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102396731859064/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100428948979812/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100598008791151/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100531730399232/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992102941173485639/bondage.gif", "https://cdn.discordapp.com/attachments/992100317430808596/992100462910251138/bondage.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🪢 **Ты** **занимаешься развратными бондажными штучками вместе с** {member.mention}')
        emb1.set_image(url=f'{random.choice(bondage)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🪢 **Ты** **занимаешься развратными бондажными штучками вместе с** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(bondage)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePlay]")
async def boobsgrab (ctx, member : nextcord.Member, *, text = None):
    boobsgrab = ["https://cdn.discordapp.com/attachments/834493654742728764/834494112286638210/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493958905659422/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493985648541776/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493853951721502/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494003180994660/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493865028616232/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493914957742110/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494014942085190/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493927197114429/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493941012758578/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493902748647424/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494053588140053/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494080339148840/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494093999734792/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494039390552114/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494066951323658/boobsgrab.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍒👐 {ctx.author.mention} **лапает грудь у** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(boobsgrab)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍒👐 {ctx.author.mention} **лапает грудь у** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(boobsgrab)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="boobsgrab", description="Лапать грудь у пользователя")
async def boobsgrab (interaction : Interaction, member : nextcord.Member, *, text = None):
    boobsgrab = ["https://cdn.discordapp.com/attachments/834493654742728764/834494112286638210/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493958905659422/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493985648541776/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493853951721502/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494003180994660/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493865028616232/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493914957742110/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494014942085190/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493927197114429/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493941012758578/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834493902748647424/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494053588140053/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494080339148840/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494093999734792/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494039390552114/boobsgrab.gif", "https://cdn.discordapp.com/attachments/834493654742728764/834494066951323658/boobsgrab.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍒👐 **Ты** **лапаешь грудь у** {member.mention}')
        emb1.set_image(url=f'{random.choice(boobsgrab)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍒👐 **Ты** **лапаешь грудь у** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(boobsgrab)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def boobsuck (ctx, member : nextcord.Member, *, text = None):
    boobsuck = ["https://cdn.discordapp.com/attachments/965983252718428230/965985028876169226/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983462442008606/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985092562473050/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983495983866007/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985802683310220/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985737621266462/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985699201425429/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985320116027472/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983534370140211/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985839802904626/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985776829628496/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985344984064000/boobsuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍒👅 {ctx.author.mention} **сосёт сиськи у** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(boobsuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍒👅 {ctx.author.mention} **сосёт сиськи у** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(boobsuck)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="boobsuck", description="Сосать сиськи у пользователя")
async def boobsuck (interaction : Interaction, member : nextcord.Member, *, text = None):
    boobsuck = ["https://cdn.discordapp.com/attachments/965983252718428230/965985028876169226/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983462442008606/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985092562473050/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983495983866007/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985802683310220/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985737621266462/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985699201425429/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985320116027472/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965983534370140211/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985839802904626/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985776829628496/boobsuck.gif", "https://cdn.discordapp.com/attachments/965983252718428230/965985344984064000/boobsuck.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍒👅 **Ты** **сосёшь сиськи у** {member.mention}')
        emb1.set_image(url=f'{random.choice(boobsuck)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍒👅 **Ты** **сосёшь сиськи у** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(boobsuck)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def creampie (ctx, member : nextcord.Member, *, text = None):
    creampie = ["https://cdn.discordapp.com/attachments/955839621902774272/955840111520649216/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840306388029460/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955839955505139752/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840159235063818/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955842304869027890/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955842659140898816/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840998074896384/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840275845115924/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840213391912960/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840066230554644/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955841342288842812/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955839871052808292/creampie.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆💦 {ctx.author.mention} **кончает в** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(creampie)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆💦 {ctx.author.mention} **кончает в** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(creampie)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="creampie", description="Кончать в пользователя")
async def creampie (interaction : Interaction, member : nextcord.Member, *, text = None):
    creampie = ["https://cdn.discordapp.com/attachments/955839621902774272/955840111520649216/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840306388029460/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955839955505139752/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840159235063818/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955842304869027890/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955842659140898816/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840998074896384/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840275845115924/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840213391912960/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955840066230554644/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955841342288842812/creampie.gif", "https://cdn.discordapp.com/attachments/955839621902774272/955839871052808292/creampie.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆💦 **Ты** **кончаешь в** {member.mention}')
        emb1.set_image(url=f'{random.choice(creampie)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍆💦 **Ты** **кончаешь в** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(creampie)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="RolePLay")
async def cum (ctx, member : nextcord.Member, *, text = None):
    cum = ["https://cdn.discordapp.com/attachments/834500528426844160/881904994863951873/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500991411945482/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500917847916605/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500964269686784/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500951191584809/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501092069998622/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501140014956624/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501065961111622/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501115449180200/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/839471906024849408/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500928869761044/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501127272923217/cum.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💦👅 {ctx.author.mention} **кончает на** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(cum)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💦👅 {ctx.author.mention} **кончает на** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(cum)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="cum", description="Кончить на пользователя")
async def cum (interaction : Interaction, member : nextcord.Member, *, text = None):
    cum = ["https://cdn.discordapp.com/attachments/834500528426844160/881904994863951873/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500991411945482/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500917847916605/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500964269686784/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500951191584809/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501092069998622/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501140014956624/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501065961111622/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501115449180200/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/839471906024849408/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834500928869761044/cum.gif", "https://cdn.discordapp.com/attachments/834500528426844160/834501127272923217/cum.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💦👅 **Ты** **кончаешь на** {member.mention}')
        emb1.set_image(url=f'{random.choice(cum)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'💦👅 **Ты** **кончаешь на** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(cum)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def dickride (ctx, member : nextcord.Member, *, text = None):
    dickride = ["https://cdn.discordapp.com/attachments/969967119469019136/969968026818580530/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969968480147357839/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967744403517520/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967825382940702/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967999471743066/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967204336549938/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967934040596500/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969968872272830474/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967859918856222/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967969511833630/dickride.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆 {ctx.author.mention} **катается на члене** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(dickride)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆 {ctx.author.mention} **катается на члене** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(dickride)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="dickride", description="Кататься на члене пользователя")
async def dickride (interaction : Interaction, member : nextcord.Member, *, text = None):
    dickride = ["https://cdn.discordapp.com/attachments/969967119469019136/969968026818580530/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969968480147357839/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967744403517520/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967825382940702/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967999471743066/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967204336549938/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967934040596500/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969968872272830474/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967859918856222/dickride.gif", "https://cdn.discordapp.com/attachments/969967119469019136/969967969511833630/dickride.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆 **Ты** **катаешься на члене у** {member.mention}')
        emb1.set_image(url=f'{random.choice(dickride)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🍆 **Ты** **катаешься на члене у** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(dickride)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolePLay]")
async def facesit (ctx, member : nextcord.Member, *, text = None):
    facesit = ["https://cdn.discordapp.com/attachments/969970754944909332/969971565989093406/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971995544526868/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971063696031764/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971096717766666/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971128468668467/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971197976657970/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971027041980457/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969972020102185020/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971959108620319/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971163793063986/facesit.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🪑 {ctx.author.mention} **сидит на лице** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(facesit)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🪑 {ctx.author.mention} **сидит на лице** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(facesit)}')
        await ctx.send(embed=emb)

@bot.slash_command(name="facesit", description="Сидеть на лице у пользователя")
async def facesit (interaction : Interaction, member : nextcord.Member, *, text = None):
    facesit = ["https://cdn.discordapp.com/attachments/969970754944909332/969971565989093406/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971995544526868/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971063696031764/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971096717766666/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971128468668467/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971197976657970/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971027041980457/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969972020102185020/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971959108620319/facesit.gif", "https://cdn.discordapp.com/attachments/969970754944909332/969971163793063986/facesit.gif"]
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🪑 **Ты** **сидишь на лице у** {member.mention}')
        emb1.set_image(url=f'{random.choice(facesit)}')
        await (interaction.response.send_message(embed=emb1))
    else:
        emb = nextcord.Embed(title='', description=f'🪑 **Ты** **сидишь на лице у** {member.mention}\n *Комментарий*: {text}')
        emb.set_image(url=f'{random.choice(facesit)}')
        await (interaction.response.send_message(embed=emb))

@bot.command(usage="[RolaPLay]")
async def finger (ctx, member : nextcord.Member, *, text = None):
    finger = ["https://cdn.discordapp.com/attachments/958005774603386881/958007818340937748/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007654524002344/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007878634053703/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007513561853983/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007592087613440/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007294594015252/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007071817760838/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007701223391292/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007761629757470/finger.gif", "https://cdn.discordapp.com/attachments/958005774603386881/958007005254140005/finger.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👇 {ctx.author.mention} **воткнул палец в** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(finger)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👇 {ctx.author.mention} **воткнул палец в** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(finger)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolaPLay]")
async def footjob (ctx, member : nextcord.Member, *, text = None):
    footjob = ["https://cdn.discordapp.com/attachments/884506240179372112/884506586196885604/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884506467409989642/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884507081099608134/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884506781299126302/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884507559057317938/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884506706317570079/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884506860911231016/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884506336732278844/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884507187127410708/footjob.gif", "https://cdn.discordapp.com/attachments/884506240179372112/884507241447837748/footjob.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🦶💦 {ctx.author.mention} **получает футджоб от** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(footjob)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🦶💦 {ctx.author.mention} **получает футджоб от** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(footjob)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def fuck (ctx, member : nextcord.Member, *, text = None):
    fuck = ["https://media.discordapp.net/attachments/736281485216317442/834505937364320316/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505616780427324/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504903023657000/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736282318788100157/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281899454169198/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504891498102814/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/881903844748046406/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504957121789993/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834506018188165160/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281834740252833/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505974165405766/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281925446139924/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504717995999282/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505950391566376/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504941166395513/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834504706431647754/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281529122029628/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505876944453692/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505605435490414/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281490484363344/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505628352512010/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505669088509970/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/736281750543532126/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505792626753566/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505696023150662/fuck.gif", "https://media.discordapp.net/attachments/736281485216317442/834505710149959710/fuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆🛏💦 {ctx.author.mention} **трахается вместе с** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(fuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆🛏💦 {ctx.author.mention} **трахается вместе с** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(fuck)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def furryfuck (ctx, member : nextcord.Member, *, text = None):
    furryfuck = ["https://cdn.discordapp.com/attachments/736283579457208414/736283835431518298/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834507078596427786/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834507010568486962/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834506853157175356/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283792360341594/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283644867379220/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834506927178383420/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283650022178907/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834507066743717908/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283808466206780/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283818163437698/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283613531734127/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283596993855548/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834506896194535534/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283618409840717/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/834506966902243348/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283623678017606/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283824652156938/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283774983340102/furryfuck.gif", "https://cdn.discordapp.com/attachments/736283579457208414/736283677222502400/furryfuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🦊💦 {ctx.author.mention} **трахается в стиле фурри с** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(furryfuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🦊💦 {ctx.author.mention} **трахается в стиле фурри с** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(furryfuck)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def handjob (ctx, member : nextcord.Member, *, text = None):
    handjob = ["https://cdn.discordapp.com/attachments/972916898436108318/972918776725114890/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972917081148391454/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972919151293235340/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972917114388238427/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972917143890952322/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972918667597721740/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972919627866832946/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972918826708652102/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972918853464121344/handjob.gif", "https://cdn.discordapp.com/attachments/972916898436108318/972919659026341989/handjob.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍆👅 {ctx.author.mention} **тебе дрочит** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(handjob)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍆👅 {ctx.author.mention} **тебе дрочит** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(handjob)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePlay]")
async def leash (ctx: nextcord.Member, *, text = None):
    leash = ["https://cdn.discordapp.com/attachments/955835975609749534/955836254405132338/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836016932032512/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836425654382672/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836092060418118/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836316136906752/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/992098924506644601/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836134854897734/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836365025738823/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836699726979102/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836549789007933/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/992098894043414559/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836190802718761/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836504767344740/leash.gif", "https://cdn.discordapp.com/attachments/955835975609749534/955836603476099122/leash.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🦮 {ctx.author.mention} **надевает этот поводок и идет за мной!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(leash)}')
        await ctx.send(embed=emb1)

@bot.command(usage="[RolePLay]")
async def masturbate (ctx, member : nextcord.Member, *, text = None):
    masturbate = ["https://cdn.discordapp.com/attachments/834831425651474442/834831683081207919/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831757462208613/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831694942044260/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831584216481802/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831815612825643/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831608800215060/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831631893135380/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831804020162660/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831769156845608/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831827457802271/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/881905216432259072/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831780376477816/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831745881997382/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831559366279178/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/958006810047045662/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831790748467220/masturbate.gif", "https://cdn.discordapp.com/attachments/834831425651474442/834831705964544071/masturbate.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'💦 {ctx.author.mention} **вам дрочит** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(masturbate)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'💦 {ctx.author.mention} **вам дрочит** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(masturbate)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def pussyeat (ctx, member : nextcord.Member, *, text = None):
    pussyeat = ["https://cdn.discordapp.com/attachments/964484282984857610/964484837744476180/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484568642125854/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775530748133486/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775911792246845/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775595931795486/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775652936601620/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484607351357521/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775394622001182/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484920548401192/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484985551740948/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484887572774972/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964485051599446016/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/1054775458006306986/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484793255460934/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964484953062670336/pussyeat.gif", "https://cdn.discordapp.com/attachments/964484282984857610/964485018485399622/pussyeat.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👅💦 {ctx.author.mention} **вашу киску лижет** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(pussyeat)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👅💦 {ctx.author.mention} **вашу киску лижет** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(pussyeat)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def spank (ctx, member : nextcord.Member, *, text = None):
    spank = ["https://cdn.discordapp.com/attachments/736274084488282113/736274160266903674/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274153820127362/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274130747523072/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274143187828757/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842062976188456/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842176428703824/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274092105269308/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842161659904100/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842136088150016/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274118776979483/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842232880234516/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842096350789692/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274138632552478/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842123806965790/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842148817862656/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274108337225818/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274115195043931/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842252601065562/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274104361025606/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842192396288040/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842212650844160/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274125311443056/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/834842075178467389/spank.gif", "https://cdn.discordapp.com/attachments/736274084488282113/736274121486237736/spank.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🍑 {ctx.author.mention} **шлёпает по попе** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(spank)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🍑 {ctx.author.mention} **шлёпает по попе** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(spank)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def strip (ctx, member : nextcord.Member, *, text = None):
    strip = ["https://cdn.discordapp.com/attachments/991784316881346601/991784604409266346/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785912402968667/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991786888086179961/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785635851538482/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787556666605608/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787670604877884/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991786585706221688/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991784967526944898/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991786363856879686/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785726549180466/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785174650077314/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991786604555423806/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787453683879967/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991786090379882637/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787181708423278/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785592281125035/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787737667621034/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991785735772459008/strip.gif", "https://cdn.discordapp.com/attachments/991784316881346601/991787148158173315/strip.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👙 {ctx.author.mention} **танцует стрип для!** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(strip)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👙 {ctx.author.mention} **танцует стрип для!** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(strip)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def tittyfuck (ctx, member : nextcord.Member, *, text = None):
    tittyfuck = ["https://cdn.discordapp.com/attachments/834844814671478824/834845106716540988/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845029348409364/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845083684962364/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834844958598758421/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834844981931409438/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834844969951952916/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845159539081226/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845041263378501/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845130196385832/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845146393739284/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845068141133874/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834844998775078952/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845053163536404/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/881905383625596959/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845094661718016/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834845117496033280/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/834844931423993946/tittyfuck.gif", "https://cdn.discordapp.com/attachments/834844814671478824/881905488055377960/tittyfuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'🥥 {ctx.author.mention} **трахает между грудями!** {member.mention}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(tittyfuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'🥥 {ctx.author.mention} **трахает между грудями!** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(tittyfuck)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def yaoifuck (ctx, member : nextcord.Member, *, text = None):
    yaoifuck = ["https://cdn.discordapp.com/attachments/736282657062912080/736283045077975081/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282769197629490/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848457453862964/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848548377591848/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283038224351272/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283049439789066/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282666126540870/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848562604802068/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282784410370148/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282873144803418/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282734363803758/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848479415107594/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283005601054860/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848505100370000/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283058642223154/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282683608662021/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848533659123723/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848443721187359/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848518304694292/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282759458193438/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/834848493922156544/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283034310934608/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282730442129498/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282790647169085/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282721147683077/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282865708564560/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282750390239425/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736283053487292446/yaoifuck.gif", "https://cdn.discordapp.com/attachments/736282657062912080/736282742261547120/yaoifuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👨🛏👨️ {ctx.author.mention} **ебёт** {member.mention} **в стиле яой!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yaoifuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👨🛏👨️ {ctx.author.mention} **ебёт** {member.mention} **в стиле яой!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yaoifuck)}')
        await ctx.send(embed=emb)

@bot.command(usage="[RolePLay]")
async def yurifuck (ctx, member : nextcord.Member, *, text = None):
    yurifuck = ["https://cdn.discordapp.com/attachments/736283166758797324/736283359470157844/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283297788854282/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283255959060520/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283456941719642/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283350062334032/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283343087206550/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283473274339388/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283405695713380/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283415682351104/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283415682351104/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283490856992858/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283284023017492/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283260031860786/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283393096024134/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283266994405406/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/834849298096717874/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283499455053854/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283431201276014/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283293082714193/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/863573933479428176/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/834849312219463680/yurifuck.gif", "https://cdn.discordapp.com/attachments/736283166758797324/736283244990955611/yurifuck.gif"]
    author = ctx.message.author
    if text == None:
        emb1 = nextcord.Embed(title='', description=f'👩🛏👩️ {ctx.author.mention} **ебёт** {member.mention} **в стиле юри!**', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb1.set_image(url=f'{random.choice(yurifuck)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👩🛏👩️ {ctx.author.mention} **ебёт** {member.mention} **в стиле юри!**\n *Комментарий*: {text}', timestamp=ctx.message.created_at, color=ctx.author.color)
        emb.set_image(url=f'{random.choice(yurifuck)}')
        await ctx.send(embed=emb)

@bot.command(name="translate")
async def translate(ctx, *, fromtext: str = None):
    if fromtext is None:
        emb = nextcord.Embed(timestamp=ctx.message.created_at)
        emb.add_field(name="Ошибка!", value=f"Непраильна пишешь! `.translate <текст>`")
        emb.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.message.author.display_avatar}")
        await ctx.send(embed=emb)
        return

    translator = Translator(to_lang="ru")
    translation = translator.translate(fromtext)

    emb1=nextcord.Embed(title=f"{translation}", timestamp=ctx.message.created_at)
    emb1.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.display_avatar}")
    await ctx.send(embed=emb1)

@bot.command(usage="[пользователь]")
async def user(ctx, *, user: nextcord.Member):
    if not user:
        user = ctx.author

    if user.bot:
        suffix = "боте!"
    else:
        suffix = "пользователе!"
    res = nextcord.Embed(
        title=nextcord.utils.escape_markdown(str(user)),
        description="Информация о " + suffix,
    )
    res.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    res.set_thumbnail(url=user.display_avatar)
    res.add_field(name="Айди:", value=user.id, inline=False)
    res.add_field(
        name="Аккаунт создан:",
        value=f"{date(user.created_at, ago=True)}",
        inline=False,
    )
    if ctx.guild:
        if user in ctx.guild.members:
            res.add_field(
                name="Участник присоединился:",
                value=f"{date(user.joined_at, ago=True)}",
                inline=False,
            )
        else:
            res.add_field(
                name="Участник присоединился:",
                value=f"{date(user.joined_at, ago=True)}",
                inline=False,
            )
    await ctx.send(embed=res)

@bot.slash_command(name="user", description="Посмотреть информацию о пользователе")
async def user(ctx, *, user: nextcord.Member):
    if not user:
        user = ctx.author

    if user.bot:
        suffix = "боте!"
    else:
        suffix = "пользователе!"
    res = nextcord.Embed(
        title=nextcord.utils.escape_markdown(str(user)),
        description="Информация о " + suffix,
    )
    res.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    res.set_thumbnail(url=user.display_avatar)
    res.add_field(name="Айди:", value=user.id, inline=False)
    res.add_field(
        name="Аккаунт создан:",
        value=f"{date(user.created_at, ago=True)}",
        inline=False,
    )
    if ctx.guild:
        if user in ctx.guild.members:
            res.add_field(
                name="Участник присоединился:",
                value=f"{date(user.joined_at, ago=True)}",
                inline=False,
            )
        else:
            res.add_field(
                name="Участник присоединился:",
                value=f"{date(user.joined_at, ago=True)}",
                inline=False,
            )
    await ctx.send(embed=res) 

@bot.command(usage="[uptime]")
async def uptime(ctx):
    await maybe_delete(ctx.message)
    diff = utcnow() - start_time
    print(start_time, diff)
    hours, seconds = diff.seconds // 3600, diff.seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    emb = nextcord.Embed(
        title=bot.user.name,
        description=f"Айди: {bot.user.id}",
        color=nextcord.Color.blue(),
        timestamp=ctx.message.created_at,
    )
    emb.add_field(
        name="Аптайм:",
        value=f"Я работаю: `{diff.days}` дней, `{hours}` часов, `{minutes}` минут, `{seconds}` секунд.",
    )
    emb.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    emb.set_footer(
        text=f"Команд: {len(bot.commands)}", icon_url=ctx.author.display_avatar
    )
    await ctx.send(embed=emb)

@bot.command(usage="[server]")
async def server(ctx):
    emb=nextcord.Embed(title=ctx.guild.name, timestamp=ctx.message.created_at, color=nextcord.Color.blue())
    emb.add_field(name='Участников:', value=ctx.guild.member_count, inline=False)
    emb.add_field(name='Ролей:', value=len(ctx.guild.roles), inline = False)
    emb.add_field(name='Владелец:', value=ctx.guild.owner.mention, inline = False)
    emb.add_field(name='Айди:', value=ctx.guild.id, inline = False)
    emb.add_field(name="server_created_name", value=f"<t:{int(ctx.guild.created_at.timestamp())}:F>, {(nextcord.utils.utcnow()-ctx.guild.created_at).days} days ago", inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
    await ctx.send(embed=emb)

@bot.slash_command(name="server", description="Посмотреть информацию о сервер")
async def server(ctx):
    emb=nextcord.Embed(title=ctx.guild.name,color=nextcord.Color.purple())
    emb.add_field(name='Участников:', value=ctx.guild.member_count, inline=False)
    emb.add_field(name='Ролей:', value=len(ctx.guild.roles), inline = False)
    emb.add_field(name='Владелец:', value=ctx.guild.owner.mention, inline = False)
    emb.add_field(name='Айди:', value=ctx.guild.id, inline = False)
    emb.add_field(name="server_created_name", value=f"<t:{int(ctx.guild.created_at.timestamp())}:F>, {(nextcord.utils.utcnow()-ctx.guild.created_at).days} days ago", inline=False)
    emb.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    await ctx.send(embed=emb) 

@bot.event
async def on_ready():
    print("BOT connected")
    await bot.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Streaming(
            name=".help | Look at About me | AkimoTop.gg", url="https://www.twitch.tv/twitch"
        ),
    )

COGS = (
    "moderation",
)

for cog in COGS:
    try:
        bot.load_extension(f'cogs.{cog}')
        print(f"Ког {cog} загружен!")
    except Exception as error:
        print(f"{cog} Ошибка!\n{error}")

print("Коги успешно загружены!")

start_time = utcnow()

bot.run('токен')