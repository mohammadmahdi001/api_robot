import telebot
import sys
import os
import json
import urllib
reload(sys)
from telebot import types
sys.setdefaultencoding("utf-8")

tokenjson = open('config.json')
tokendata = json.loads(tokenjson)
TOKEN = tokendata['token']
bot = telebot.TeleBot(TOKEN) # Add token json  . config.json

@bot.message_handler(func=lambda message: True)
def m(m):
    if m.text == '/start' or m.text == '/help':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        key_p = types.KeyboardButton('Admin\xE2\x98\x95\xEF\xB8\x8F')
        key_c = types.KeyboardButton('Time\xE2\x8F\xB1')
        sticker = types.KeyboardButton('Sticker')
        markup.add(key_p, key_c)
        markup.add(sticker)
        bot.send_chat_action(m.chat.id, 'typing')
        bot.reply_to(m, "Hi {}".format(m.from_user.first_name))
        bot.send_message(m.chat.id, 'This is a test telegram bot', reply_markup=markup)
        print 'command help'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
        return
    if m.text == 'Admin\xE2\x98\x95\xEF\xB8\x8F':
        bot.send_message(m.chat.id, '@negative_officiall')
        print 'command admin'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == 'Time\xE2\x8F\xB1':
        url = "http://api.gpmod.ir/time/"
        response = urllib.urlopen(url)
        data = response.read()
        parsed_jsonss = json.loads(data)
        ENtime = (parsed_jsonss['ENtime'])
        bot.send_message(m.chat.id, ENtime)
        print 'command time'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == 'Sticker':
        urllib.urlretrieve("https://source.unsplash.com/random", "img.jpg")
        bot.send_chat_action(m.chat.id, 'upload_photo')
        bot.send_sticker(m.chat.id, open('img.jpg'))
        print 'command Sticker'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == '/leave':
        bot.leave_chat(m.chat.id)
        print 'command leave'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)


bot.polling(none_stop=True, timeout=20)
