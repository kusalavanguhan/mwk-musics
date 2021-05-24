import requests
from pyrogram import Client as bot

from samantha.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from samantha.Services.Callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
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
