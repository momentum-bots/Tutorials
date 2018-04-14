import telebot

token = '589185387:AAGnksqxilzc9GN3y7aVjlJPsN2oDsuAbFg' # Вставь свой токен
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
