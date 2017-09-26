import telebot
import constants;

import sys
print sys.getdefaultencoding()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

bot = telebot.TeleBot(constants.token)

# bot.send_message(265468391, "TestMessage")

# upd = bot.get_updates();

# -*- coding: utf-8 -*-



@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.send_message(message.chat.id, "Helpful message")


# start is the first command from user


@bot.message_handler(commands=['start'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    user_markup.row("/Hot", "/Cold", "/Food")
    bot.send_message(message.from_user.id, "Hi! What do you want to order", reply_markup=user_markup)
    user_markup.


@bot.message_handler(commands=['Hot'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    user_markup.row("Tea", "Coffee")
    bot.send_message(message.from_user.id, "KJKK", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "text":
        bot.send_message(message.chat.id, "alive")
    elif message.text == "t2":
        bot.send_message(message.chat.id, "kiddin")


bot.polling(none_stop=True, interval=0)
