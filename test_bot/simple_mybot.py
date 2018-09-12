from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import logging
import sys
import argparse
import ephem
from settings import Configs


PLANETS = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon', 'Phobos',
           'Deimos', 'Io', 'Europa', 'Ganymede', 'Callisto', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan',
           'Hyperion', 'Iapetus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda']


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    print("Run /start")


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_info(bot, update, args):
    answer = args[0].capitalize()

    if answer in PLANETS:
        try:
            planet = getattr(ephem, answer)(datetime.today().strftime('%Y/%m/%d'))
            update.message.reply_text(f"Today {answer} in {ephem.constellation(planet)[1]}")
        except AttributeError:
            update.message.reply_text("Ooops, Something went wrong")
    else:
        update.message.reply_text("Not found planet {}".format(answer))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='usage -c /path/to/config.yaml')
    args = parser.parse_args()

    if args.config:
        bot_conf = Configs(args.config)
    else:
        bot_conf = Configs()

    proxy_data = bot_conf.get_proxy_data()
    key = bot_conf.get_telegram_token()
    mybot = Updater(key, request_kwargs=proxy_data)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("ephem", planet_info, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()