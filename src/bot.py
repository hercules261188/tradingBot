import telebot
from keys import api_key
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '🇷🇺 Привет, ты написал мне /start. '
                                      'Этот бот ещё в разработке, но в планах разработчика @WhatIsLove0770 добавить в '
                                      'него функции трейдинга и арбитража\n\n\n'
                                      '🇬🇧 Hi, you wrote me /start. This bot is still in development, but developer '
                                      '@ WhatIsLove0770 plans to add trading and arbitrage functions to it.')

@bot.message_handler(commands=['connect_arbitrage'])
def connect_arbitrage():
    pass

bot.polling(none_stop=True)