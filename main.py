import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5258593695:AAEXa4z_d_LRj6XN_tyulkil8RDeR2mCC_0"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=['start'])
def send1(message):
    bot.send_message(chat_id=message.chat.id, text="- The Bot Is Running ....")
@bot.message_handler(commands=['get'])
def send(message):
    uid = '7869020'#message.text.replace("/get ", '')
    file = requests.get("https://pastebin.com/raw/0kPLPnxC").text.splitlines()
    numD = 0
    numL = 0
    numE = 0
    numW = 0
    infoM = bot.send_message(chat_id=420953620, text=f"- ID : {uid}\nDone Check : {numL}\nDone Send : {numD}\nDon't Have Coins : {numE}\nDon't Send : {numW}")
    while True:
        fil = file[numL]
        url = requests.get(f"https://m0hmdhaider.000webhostapp.com/mido.php?target={fil}&userid={uid}&submit=submit").text
        if "DONE :" in url:
            numF1 = url.split("DONE : ")[1]
            numF = (numF1[0] + numF1[1] + numF1[2] + numF1[3]).replace("<", '')
            bot.send_message(chat_id= 420953620, text=f"- ID : {uid}\n- Done Send Followers Count : {numF} ..")
            numD += 1
            numL += 1
            bot.edit_message_text(chat_id= 420953620 , message_id=infoM.message_id, text=f"- ID : {uid}\nDone Check : {numL}\nDone Send : {numD}\nDon't Have Coins : {numE}\nDon't Send : {numW}")

        elif "Sending orders less than 150 is temporarily disabled. Please try again in another hour." in url:
            numL += 1
            numE += 1
            bot.edit_message_text(chat_id= 420953620 , message_id=infoM.message_id, text=f"- ID : {uid}\nDone Check : {numL}\nDone Send : {numD}\nDon't Have Coins : {numE}\nDon't Send : {numW}")

        elif '"You have to wait until the previous order is completed."' in url:
            numW +=1
            bot.send_message(chat_id= 420953620, text= f"ID : {uid}\n- Sleep 15 minutes ....")
            bot.edit_message_text(chat_id= 420953620 , message_id=infoM.message_id, text=f"- ID : {uid}\nDone Check : {numL}\nDone Send : {numD}\nDon't Have Coins : {numE}\nDon't Send : {numW}")
            time.sleep(900)
        else:
            numL += 1
            bot.edit_message_text(chat_id=420953620, message_id=infoM.message_id,text=f"- ID : {uid}\nDone Check : {numL}\nDone Send : {numD}\nDon't Have Coins : {numE}\nDon't Send : {numW}")

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://mmdhsbdbot.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
