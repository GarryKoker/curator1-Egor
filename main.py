# подключил библиотеку (изи)
import telebot

bot = telebot.TeleBot("7403214410:AAGPtnInMcPEI-_mNELJpV_1afqjacCxVAc")


# Ряд сложных манипуляций
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Дароу")


@bot.message_handler(commands=["end"])
def end_handler(message):
    bot.send_message(message.chat.id, "Конец")


@bot.message_handler(commands=["link"])
def link_handler(message):
    bot.send_message(message.chat.id, "[Кинь заявку в др](https:/vk.com/khaupshevv)", parse_mode="Markdown")


bot.infinity_polling()








