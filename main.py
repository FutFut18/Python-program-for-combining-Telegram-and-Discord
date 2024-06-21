import telebot
import time
import threading
tgtokenread = open("telegram.txt", "r+", encoding='utf-8')
TOKEN = tgtokenread.read()
tgtokenread.close()
global count
count = 0
tgidread = open("chatidtelegram.txt", "r+", encoding='utf-8')
TGCHATID = tgidread.read()
tgidread.close()

bot = telebot.TeleBot(TOKEN)
def scan():
    b = 0
    while True:
        with open("data1.txt", "r+", encoding="utf-8") as data:

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
                    bot.send_message(TGCHATID, text)
            else:
                1
@bot.message_handler()
def accept(message):
    #print(message.chat.id, "user_id:" , message.from_user.id , ", first name:" , message.from_user.first_name , ", last name:" , message.from_user.last_name , ", username:" , message.from_user.username , ", language code:" , message.from_user.language_code , ", text:" , message.text)
    if str(message.chat.id) == str(TGCHATID):
        with open("data.txt", "w", encoding='utf-8') as data:
            global count
            count += 1
            if count == 10:
                count = 0
            data.write(str(count))
            data.write(str(message.from_user.first_name) + " (@" + str(message.from_user.username) + ")" ": " + str(message.text))
            data.close()
        #print(count)

thread5 = threading.Thread(target=scan, name="Thread-5")
thread5.start()
bot.infinity_polling()