


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = """
👋🏻 **Hi [{}](tg://user?id={})**,\nI'm **Samantha 😌** \nA Private Group Manager Bot Designed for Some Specific Groups... 🤷‍♀️\nOnly My Dev can manage me... 😉\nDo You Know A secret... **"im a different bot"**\nMade with ❤️ By @shamilnelli!"
"""

HELP = """
**Need Help 🤭**

👉 **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it
\u2022 `/help` shows help for commands
\u2022 `/playlist` shows the playlist
\u2022 `/current` shows playing time of current track
\u2022 `/song` [song name] download the song as audio

👉 **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/mwk` check Current Vc
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

👉 **Developer: @shamilnelli** 💞
"""

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
        InlineKeyboardButton('UPDATES CHANNEL', url='https://t.me/mwklinks'),
        InlineKeyboardButton('SUPPORT GROUP', url='https://T.me/redbullfed'),
    ],
    [
        InlineKeyboardButton('DONATE', url='https://t.me/shamilhelpbot'),
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
