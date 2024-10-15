import telebot
import os
from random import choice

API_TOKEN = '8056447024:AAEehoWZKIvZ05pfPw1dEzqGU44gaC2JD3g'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(f'images/{choice(os.listdir("images"))}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


@bot.message_handler(commands=['animals'])
def send_mem(message):
    with open(f'animals/{choice(os.listdir("animals"))}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()