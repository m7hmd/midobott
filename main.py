import requests, user_agent, json, flask, telebot, random, os, sys, time, threading
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5295940154:AAGZc95-F6VltntXMGDGIsyRb21qI8EIZwQ"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

def S(msgt, mesgchat):
    if msgt == "/start":
        bot.send_message(mesgchat, "Send List ......")
    elif "/" in message.text:
        bot.send_message(mesgchat, "Send List ......")
    else:
        mes = msgt.splitlines()
        for username in mes:
            username1 = username.replace("@", "")
            url = "https://t.me/" + str(username1)
            headers = {
                "User-Agent": generate_user_agent(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
            response = requests.get(url, headers=headers).text
            if "Send Message" in response:
                if "bot" not in username1:
                    if "@" in username:
                        bot.send_message(mesgchat, f"{username} is account")
                    else:
                        bot.send_message(mesgchat, f"@{username} is account")

            elif "subscribers" in response or "Preview channel" in response or "subscriber":
                print("hello")
            time.sleep(5)
        bot.send_message(mesgchat, f"Done list begin with {mes[0]}")

@bot.message_handler(content_types=["text"])
def Send(message):
    threading.Thread(target=S,args=[message.text, message.chat.id]).start()

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
