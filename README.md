# Mwk - Musics
Powerfull VC music streamer Radio bot for tg

<h2 align="centre">MwK Musics 🎵</h2>

## Deploy

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Heroku Vars:
1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get From my.telegram.org
3. `BOT_TOKEN` : Get it From @Botfather
4. `SESSION_STRING` : Generate From [@genStr robot](http://t.me/genStr_robot).
5. `CHAT` : ID of Channel/Group where the bot plays Music/Radio.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group.
7. `ADMINS` : ID of users who can use admin commands.
8. `STREAM_URL` : Stream URL of radio station to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku.
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy. 
- 24x7 Music even if heroku restarts, radio stream restarts automatically.  
- To play a song just send the audio file to Bot or reply to an audio with `/play` to start playing it in the voice chat.
- To download audio you can use `/song` command to the bot.
- Use `/help` to know about other commands & its usage.

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/genStr_robot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## Run On VPS (The Hard Way)

```sh
$ git clone https://github.com/shamilhabeebnelli/mwk-musics
$ cd mwk-musics
$ sudo apt-get install ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
```
Edit **config.py** with your own values.

```sh
$ python3 main.py
```

### A bot that can play music on telegram group's voice call & download songs from yt

### Update Channel:

<a href="https://t.me/redbullfed"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Channel-blue.svg?logo=telegram"></a>

### Film Group:

<a href="https://t.me/movieworldkdy"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>
