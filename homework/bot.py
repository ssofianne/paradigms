import telebot;
from telebot import types

bot = telebot.TeleBot('6544409406:AAHyoSCaHBqyUG1zyfZK71Jbb4JMZmfGMII');

state = "country"

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Меня зовут Хвашик, я бот-географ.\n\n<b>Вот мой список команд:</b>\n/start - список команд\n/capital - столица страны\n/language - язык страны\n/photo - фото страны\n/flag - флаг страны'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    
countries_info = [
    {"name": "Россия", "capital": "Москва", "language": "русский", "photo": r"россия.jpg", "flag":"флаг россии.png"},
    {"name": "Япония", "capital": "Токио", "language": "японский", "photo": r"япония.jpg", "flag":"флаг японии.png"},
    {"name": "США", "capital": "Вашингтон", "language": "английский", "photo": r"сша.jpg", "flag":"флаг сша.png"},
    {"name": "Великобритания", "capital": "Лондон", "language": "английский","photo": r"лондон.jpg", "flag":"флаг великобритании.png"},
    {"name": "Южная Корея", "capital": "Сеул", "language": "корейский","photo": r"юж корея.jpg", "flag":"флаг юж кореи.png"},
    {"name": "Франция", "capital": "Париж", "language": "французский","photo": r"франция.jpg", "flag":"флаг франции.png"},
    {"name": "Китай", "capital": "Пекин", "language": "китайский","photo": r"китай.jpg", "flag":"флаг китая.png"},
    {"name": "Австралия", "capital": "Канберра", "language": "австралийский","photo": r"австралия.jpg", "flag":"флаг австралии.png"},
    {"name": "Бразилия", "capital": "Бразилиа", "language": "бразильский португальский","photo": r"бразилия.jpg", "flag":"флаг бразилии.png"},
    {"name": "Литва", "capital": "Вильнюс", "language": "литовский","photo": r"литва.jpg", "flag":"флаг литвы.png"},
    {"name": "Германия", "capital": "Берлин", "language": "немецкий","photo": r"германия.jpg", "flag":"флаг германии.png"},
    {"name": "Греция", "capital": "Афины", "language": "греческий","photo": r"греция.jpg", "flag":"флаг греции.png"},
    {"name": "Армения", "capital": "Ереван", "language": "армянский","photo": r"армения.jpg", "flag":"флаг армении.png"},
]

@bot.message_handler(func=lambda message: message.text == "/capital")
def handle_country_request(message):
    global state
    state = "country"
    bot.send_message(message.chat.id, text="Напишите название страны, а я скажу ее столицу.", parse_mode='html')

@bot.message_handler(func=lambda message: any(country["name"] == message.text for country in countries_info))
def get_country_info(message):
    print(state)
    match state:
        case "country": 
            country_name = message.text
            for country in countries_info:
                if country["name"] == country_name:
                    result = country["capital"]
                    response_text = f"Столица этой страны - <b>{result}</b>."
                    bot.send_message(message.chat.id, text=response_text, parse_mode='html')
                    break
            else:
                bot.send_message(message.chat.id, text="Извините, я не знаю столицу этой страны.", parse_mode='html')
        case "lang":
            print("aa")
            country_name = message.text
            for country in countries_info:
                    if country["name"] == country_name:
                        result = country["language"]
                        response_text = f"Язык этой страны - <b>{result}</b>."
                        bot.send_message(message.chat.id, text=response_text, parse_mode='html')
                        break
            else:
                bot.send_message(message.chat.id, text="Извините, я не знаю язык этой страны.", parse_mode='html')
        case "photo":
            print("oo")
            country_name = message.text
            for country in countries_info:
                    if country["name"] == country_name:
                        result = open(country["photo"],'rb')
                        bot.send_message(message.chat.id, text="У меня есть такое фото:", parse_mode='html')
                        bot.send_photo(message.chat.id,result)
                        break
            else:
                bot.send_message(message.chat.id, text="Извините, у меня нет фото этой страны.", parse_mode='html')
        case "flag":
            print("jj")
            country_name = message.text
            for country in countries_info:
                    if country["name"] == country_name:
                        result = open(country["flag"],'rb')
                        bot.send_message(message.chat.id, text="Флаг этой страны:", parse_mode='html')
                        bot.send_photo(message.chat.id,result)
                        break
            else:
                bot.send_message(message.chat.id, text="Извините, у меня нет фото этой страны.", parse_mode='html')
@bot.message_handler(func=lambda message: message.text == "/photo")
def handle_photo_request(message):
    global state
    state = "photo"
    bot.send_message(message.chat.id, text="Напишите название страны, а я покажу ее фото.", parse_mode='html')

            
@bot.message_handler(func=lambda message: message.text == "/language")
def handle_language_request(message):
    global state
    state = "lang"
    bot.send_message(message.chat.id, text="Напишите название страны, а я скажу ее язык.", parse_mode='html')
    
@bot.message_handler(func=lambda message: message.text == "/flag")
def handle_flag_request(message):
    global state
    state = "flag"
    bot.send_message(message.chat.id, text="Напишите название страны, а я покажу ее флаг.", parse_mode='html')


bot.polling(non_stop=True)
