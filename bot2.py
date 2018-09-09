# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging

logging.basicConfig(format=('%(name)s - %(levelname)s - %(message)s'), level=logging.INFO, filename='bot2.log')


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater('633757676:AAH_S7DJjOf7gRxKp4V1lPMxoHIdRpf3X5k', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def create_planet_obj(name):
    function = getattr(ephem, name, None)
    if function is None:
        return None
    return function()


def planet(bot, update):
    command = update.message.text
    planets = command.split()
    if len(planets) != 2:
        update.message.reply_text('InvalidCommand')
        return
    planet_name = planets[1]
    planet = create_planet_obj(planet_name)
    if planet is None:
        update.message.reply_text('InvalidPlanetName')
        return
    planet.compute()
    const = ephem.constellation(planet)
    update.message.reply_text('Planet ' + planet_name + ' is in constellation ' + const[1])


# Вызываем функцию - эта строчка собственно запускает бота
main()
