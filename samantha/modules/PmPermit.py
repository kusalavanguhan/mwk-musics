from pyrogram import filters
from pyrogram.types import Message

from samantha.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Hi there, No Hi - No Kooi...🤫 For 🎵 songs Join @mwksongs | For 🎬 Movies Join @movieworldkdy | 🛠 Support Group @redbullfed 😌,
    )
    return
