import nextcord
import time
import threading
import asyncio
dstokenread = open("discord.txt", "r+", encoding='utf-8')
TOKENDS = dstokenread.read()
dstokenread.close()

intents = nextcord.Intents.default()
intents.message_content = True
text = "21"
botDS = nextcord.Client(intents=intents)
count = 1
def scan():
    b = 0
    while True:
        with open("data.txt", "r+", encoding="utf-8") as data:

            a = data.read()
            if len(a) > 0 and a[0].isdigit():
                if int(a[0]) == b:
                    1
                else:
                    print(a)
                    b = int(a[0])
                    time.sleep(0.1)
                    data.close()
                    global text
                    text = a[1:999]
                    asyncio.run_coroutine_threadsafe(send_message(text), botDS.loop)
            else:
                1

@botDS.event
async def on_message(message):
    if message.author == botDS.user:
        return
    else:
        global text
        #await message.channel.send(message.content)
        #print(message.channel.send, message.author.name, text)
        with open("data1.txt", "w", encoding='utf-8') as data:
            global count
            count += 1
            if count == 10:
                count = 0
            data.write(str(count))
            data.write(str(message.author.global_name) + " (@" + str(message.author) + ")" ": " + str(message.content))
            #print(message)
            data.close()
        #print(count)

async def send_message(text):
    dsidread = open("chatiddiscord.txt", "r+", encoding='utf-8')
    channel_id = str(dsidread.read())
    dsidread.close()
    channel = botDS.get_channel(int(channel_id))
    await channel.send(text)

thread2 = threading.Thread(target=scan, name="Thread-2")
thread2.start()
botDS.run(TOKENDS)