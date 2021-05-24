import logging
from samantha.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from samantha.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎬 Fɪʟᴍ Gʀᴏᴜᴩ", url=f"https://t.me/movieworldkdY")],
                [
                    InlineKeyboardButton(
                        "👨‍🔬 My Dᴇᴠ", url=f"https://t.me/shamilnelli"), 
                    InlineKeyboardButton(
                        "🛠 Suᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/redbullfed")
                ],[
                    InlineKeyboardButton(
                        "🎵 Mᴜꜱɪᴄ Gʀᴏᴜᴩ", url=f"https://t.me/mwksongs")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Suᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/redbullfed"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/redbullfed"
        button = [
            [InlineKeyboardButton(text = '🎬 Fɪʟᴍ Gʀᴏᴜᴩ', url=f"https://t.me/movieworldkdy")],
            [InlineKeyboardButton(text = '👨‍🔬 My Dᴇᴠ', url=f"https://t.me/shamilnelli"),
             InlineKeyboardButton(text = '📞 Suᴩᴩᴏʀᴛ Gʀᴏᴜᴩ', url=f"https://t.me/redbullfed")],
            [InlineKeyboardButton(text = '🛠 Source Code 🛠', url=f"https://github.com/shamilhabeebnelli/samanthaXcalls")],
            [InlineKeyboardButton(text = '🛠', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hey there! My name is samantha.
I'm a Queen for helping admins of TEAM MWK to manage their groups, Have a look at the following for an idea of some of the things I can help you with**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡 Click here for help 🟡", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )
