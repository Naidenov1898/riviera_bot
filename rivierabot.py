import telebot 
from telebot import types 
import riviera_bot.config as config 

bot = telebot.TeleBot(config.token) 
 
@bot.message_handler(commands=['number']) 
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) 
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Номер телефона', reply_markup=keyboard)
 
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        print(message.contact)

@bot.message_handler(content_types=['contact'])
def checking_numbers(message):
    try:
        if message.contact.user_id == message.from_user.id:
            message.contact.phone_number
    except Exception as error:
        print(error)
        bot.send_message(message.chat.id, 'Номер не определен!')


bot.polling()