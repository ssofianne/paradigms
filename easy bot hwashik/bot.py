import telebot;
from telebot import types

bot = telebot.TeleBot('6544409406:AAHyoSCaHBqyUG1zyfZK71Jbb4JMZmfGMII');

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Меня зовут Хвашик.'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
    btn0 = types.KeyboardButton("Приветствие")
    btn1 = types.KeyboardButton("Что ты умеешь?")
    btn2 = types.KeyboardButton("Покажи фото страны")
    btn3 = types.KeyboardButton("Назови столицу страны")
    markup.add(btn0, btn1, btn2, btn3)
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def f(message):
    
    if (message.text == "Что ты умеешь?"):
         bot.send_message(message.chat.id, text="Я знаю столицы некоторых стран и могу показать их фото!")

    elif ( message.text == "Приветствие"):
        bot.send_message(message.chat.id, text="Привет, нажми на любую кнопку.")
        

        
    elif ( message.text == "Покажи фото страны"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
        rus = types.KeyboardButton("Фото России")
        yap = types.KeyboardButton("Фото Японии")
        usa = types.KeyboardButton("Фото США")
        fra = types.KeyboardButton("Фото Франции")
        kit = types.KeyboardButton("Фото Китая")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(rus, yap, usa, fra, kit, back)
        bot.send_message(message.chat.id, text="У меня есть фотографии этих стран", reply_markup=markup)
    elif (message.text == "Фото России"):
        photo = open('россия.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    elif (message.text == "Фото Японии"):
        photo = open('япония.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    elif (message.text == "Фото США"):
        photo = open('сша.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    elif (message.text == "Фото Франции"):
        photo = open('франция.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    elif (message.text == "Фото Китая"):
        photo = open('китай.jpg','rb')
        bot.send_photo(message.chat.id,photo)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width = 1)
        button0 = types.KeyboardButton("Приветствие")
        button1 = types.KeyboardButton("Что ты умеешь?")
        button2 = types.KeyboardButton("Покажи фото страны")
        button3 = types.KeyboardButton("Назови столицу страны")
        markup.add(button0, button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup) 


    elif ( message.text == "Назови столицу страны"):
         bot.send_message(message.chat.id, text="Напишите название страны, а я скажу ее столицу.",parse_mode='html')
    elif (message.text == "Россия"):
         bot.send_message(message.chat.id, text="Столица России - <b>Москва</b>.",parse_mode='html')
    elif (message.text == "Япония"):
         bot.send_message(message.chat.id, text="Столица Японии - <b>Токио</b>.",parse_mode='html')
    elif (message.text == "США"):
         bot.send_message(message.chat.id, text="Столица США - <b>Вашингтон</b>.",parse_mode='html')
    elif (message.text == "Франция"):
         bot.send_message(message.chat.id, text="Столица Франции - <b>Париж</b>.",parse_mode='html')
    elif (message.text == "Китай"):
         bot.send_message(message.chat.id, text="Столица Китая - <b>Пекин</b>.",parse_mode='html')
    elif (message.text == "Германия"):
         bot.send_message(message.chat.id, text="Столица Германии - <b>Берлин</b>.",parse_mode='html')
         

        
    else:
        bot.send_message(message.chat.id, text="Извините, я не знаю такую страну...",parse_mode='html')
    

                     
bot.polling(non_stop=True)
