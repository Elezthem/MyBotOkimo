from nextcord import Message


async def maybe_delete(message: Message):
    me = message.guild.me if message.guild else message.channel.me
    if (
        message.author == me
        or message.channel.permissions_for(me).manage_messages
    ):
        await message.delete()
        return True
    return False
