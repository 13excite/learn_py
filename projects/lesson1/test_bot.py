from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import sys
import argparse

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python', },
}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def get_key(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()[0].rstrip()
    except IOError as err:
        print("Can't get key with error: {}".format(err))
        sys.exit(1)



def greet_user(bot, update):
    print("Run /start")


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', '-k', required=True, help='specify the path to  key file')
    args = parser.parse_args()

    key = get_key(args.key)
    mybot = Updater(key, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()