from pyrogram import Client, filters
from pyrogram.types import Message
from shamil.voicechat import mp, RADIO
from config import Config
STREAM_URL=Config.STREAM_URL
ADMINS=Config.ADMINS

@Client.on_message(filters.command("radio") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text("**Please Stop Existing Radio Stream /stopradio!**")
        return
    await mp.start_radio()
    await message.reply_text(f"**Yeah Boy Started Radio Streaming:** <code>{STREAM_URL}</code> 😌")

@Client.on_message(filters.command("stopradio") & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text("**Please Start A Radio Stream First /radio!**")
        return
    await mp.stop_radio()
    await message.reply_text("**Radio Stream Ended Successfully! 😐**")
