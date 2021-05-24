import requests
from pyrogram import Client as Bot

from samantha.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from samantha.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/tg_vc_bot.jpg", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="samantha.modules"),
)

bot.start()
run()
