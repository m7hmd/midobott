import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
import threading
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5285309268:AAHHPhigkibAd57942s_QsBnoAWMikAdRWE"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
f = []
b = '1234567890qwertyuiopasdfghjklzxcvbnm-_'
a = 'qwertyuiopasdfghjklzxcvbnmcvbnm'

for g in a:
    for i in b:
        f.append(f"{i}{g}{g}{g}{g}{g}")
        f.append(f"{g}{i}{g}{g}{g}{g}")
        f.append(f"{g}{g}{i}{g}{g}{g}")
        f.append(f"{g}{g}{g}{i}{g}{g}")
        f.append(f"{g}{g}{g}{g}{i}{g}")
        f.append(f"{g}{g}{g}{g}{g}{i}")


bot = telebot.TeleBot("5285309268:AAHHPhigkibAd57942s_QsBnoAWMikAdRWE")
#bot.send_message(chat_id=-1001637373978, text="hello")
print("bot started .. ")
def check(listt, message):
  x = 1
  for username in listt:
    username1 = username.replace("@", "")
    url = "https://tamtam.chat/" + str(username1)
    headers = {
      "User-Agent": generate_user_agent(),
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    response = requests.get(url, headers=headers)
    if "Public channel" in response.text or "Open channel" in response.text:
      if 'data-url="' in response.text :
          if response.text.split("<h1>")[1].split("</h1>")[0] == "Zaid":
                responseTime = requests.get(str((response.text.split('data-url="')[1]).split('">')[0])).text.split("<time>")[1].split(" </time>")[0]
                time = responseTime.replace('января в', '1').replace('февраля в', '2').replace('марта в', '3').replace('мая', '5').replace('июля', '7').replace('августа', '8').replace('октября', '10').replace('апреля', '4').replace('сентября', '9').replace('ноября', '11').replace('декабря', '12').replace(' ', '-')
                bot.send_message(chat_id=-1001637373978, text=f"URL :: {url}\nTime :: {time}")
      else:
          if response.text.split("<h1>")[1].split("</h1>")[0] == "Zaid":
                bot.send_message(chat_id=-1001637373978, text=f"URL :: {url}\nTime :: Don't Have Post")
    print(f'[{str(x)}] {username1}')
    x += 1
  bot.send_message(chat_id=919505317, text='Done : '+listt[0])


@bot.message_handler(content_types=["text"])
def S(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, f"send ...")
        print("hi")
    elif "/" in message.text:
        bot.send_message(message.chat.id, "Send List ......")
        print("hi")
    else:
        threading.Thread(target=check, args=[f, message]).start()

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://temidolebot.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
