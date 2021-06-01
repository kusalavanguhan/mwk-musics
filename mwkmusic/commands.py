


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = """
👋🏻 **Hi [{}](tg://user?id={})**,\nI'm **Samantha 😌** \nA Private Group Manager Bot Designed for Some Specific Groups... 🤷‍♀️\nOnly My Dev can manage me... 😉\nDo You Know A secret... **"im a different bot"**\nMade with ❤️ By @shamilnelli!"
HELP = "**Do You Want Help... Huh!!! 🤭**
"""

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('MOVIE GROUP', url='https://t.me/movieworldkdy'),
        InlineKeyboardButton('MUSIC GROUP', url='https://t.me/mwksongs'),
    ],
    [
        InlineKeyboardButton('UPDATES CHANNEL', url='https://t.me/mwklinks'),
        InlineKeyboardButton('TECH GROUP', url='https://T.me/redbullfed'),
    ],
    [
        InlineKeyboardButton('FILM UPDATES', url='https://t.me/redbull_status'),
        InlineKeyboardButton('DEVELOPER', url='https://t.me/shamilnelli'),
    ],
    [
        InlineKeyboardButton('⚙️ SOURCE CODE ⚙️', url='https://github.com/shamilhabeebnelli/mwk-musics'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
