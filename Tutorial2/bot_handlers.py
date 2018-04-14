from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений


@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)