from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import logging
import re
import argparse
import ephem
from settings import Configs

a= '(^".+"$)|(^\'.+\'$)'
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


def wordcount_parser(phrase, regexp, regexp_empty_string='(^""$)|(^\'\'$)'):
    pattern = re.compile(regexp)
    if pattern.match(phrase):
        return f"words count = {len(phrase.split(' '))}"
    elif pattern.match(regexp_empty_string):
        return "Empty string between qoutes"
    else:
        return "Incorrect phrase"


def word_count(bot, update):
    user_input = update.message.text.split('wordcount')[1][1:]
    print(user_input)
    parsing_text = wordcount_parser(user_input, '(^".+"$)|(^\'.+\'$)')
    print(parsing_text)
    update.message.reply_text(parsing_text)


def calculate_input(calc):
    if calc.endswith('='):
        num_list = re.split("\+|\-|\/|\*", calc[:-1])
        if len(num_list) > 1:
            try:
                int(num_list[0])
                int(num_list[1])
                return eval(calc[:-1])
            except ZeroDivisionError:
                return "You can't divide by 0"
            except ValueError:
                return "Oops, Value error, usage only number"
        else:
            return f"Not calculate {calc[:-1]}. Usage /calc num(action)num="


def calculate(bot, update, args):
    print(args)
    answer = calculate_input(args[0])
    update.message.reply_text(answer)


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
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("calc", calculate, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()