# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# Функция будет вызываться, когда пользователь в чате напишет /start вручную или подключится к боту в первый раз
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("581633010:AAFJin9MwlMm_cB91QEmbvfKzZPL18dUYcE", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
