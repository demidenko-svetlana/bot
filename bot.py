from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def main():
    mybot = Updater("1076580938:AAH_oNs7W5YfTmpOC75DjBBcO4y2vXSJno4", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling() #проверка, есть ли что-то новое
    mybot.idle()

def greet_user(bot, update):
    print('Вызван /start') 
    print(update)

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)    

main()    