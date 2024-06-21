# Python-program-for-combining-Telegram-and-Discord
By running this on your computer or server, you will be able to combine your Discord channel and a Telegram group to communicate with participants without having to have both applications.

To get started, you should install Python 3 in any way convenient for you (I used Python 3.8 during development)

You need to install the libraries:
- pytelegrambotapi
- nextcord
- asyncio

The way to install the library:
- pip install nextcord

You need to change several files:
- telegram.txt : Write down the token of your Telegram bot here
- discord.txt : Write down the token of your Discord bot here
- chatidtelegram.txt: Write down the ID of your Telegram chat here
- chatiddiscord.txt: Write down the ID of your Discord channel here

To run the program, you must run 2 files:
- main.py
- discordbot.py

Your discord bot must have permission to read messages, it is issued in the Discord developer portal
Your telegram bot must have permission to read messages from the group, it is issued in @BotFather
