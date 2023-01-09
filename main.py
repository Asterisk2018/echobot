import telebot

TOKEN = "5778336111:AAGfrNkoReWncsjKo20ervETxSdmvxOEoBI"

bot = telebot.TeleBot(TOKEN)
name = 'Анастасия'
@bot.message_handler(content_types=["text"])
def echo(message):
    if  name  in message.text:
       bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
       bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
