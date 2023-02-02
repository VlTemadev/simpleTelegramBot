import telebot
from settings import token, bot_url

bot = telebot.TeleBot(token)

print(f"Bot Started!. Follow the link {bot_url}")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>. Бот создали Аня и Артём. В нашем боте вы найдете много обучающего контента на разные тематики.\n" \
           "Для простотра введите команду: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["help"])
def help(message):
    mess = "Лист курсов\n" \
           "1. Программирование - /Programming \n" \
           "2. Видеомонтаж- /VideoEditing \n" \
           "3. Обработка фотографий - /PhotoProcessing \n" \
           "4. Рисование в Adobe Photoshop - /Painting \n" \
           "5. UX - UI Дизайн - /Design \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["Programming"])
def Programming(message):
    mess = "Лист курсов\n" \
           "1. Базовый курс по JavaScript - /js \n" \
           "2. Базовый курс по C# - /c# \n" \
           "3. Базовый курс по C++ - /c++ \n" \
           "4. Базовый курс по React - /react \n" \
           "5. Базовый курс по Python - /python \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["VideoEditing"])
def VideoEditing(message):
    mess = "Лист курсов\n" \
           "1. Склейка и обрезка видео - /videolesson1 \n" \
           "2. Кадр - /videolesson2 \n" \
           "3. DaVinci Resolve 17 для НОВИЧКОВ - /videolesson3 \n" \
           "4. Монтаж в DaVinci Resolve - /videolesson4 \n" \
           "5. Курс по Davinci Resolve - /videolesson5 \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["PhotoProcessing"])
def PhotoProcessing(message):
    mess = "Лист курсов\n" \
           "1. Обработка в Lightroom - /photolesson1 \n" \
           "2. Ретушь кожи в photoshop- /photolesson2 \n" \
           "3. DaVinci Resolve 17 для НОВИЧКОВ - /photolesson3 \n" \
           "4. Монтаж в DaVinci Resolve - /photolesson4 \n" \
           "5. Курс по Davinci Resolve - /photolesson5 \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["Painting"])
def Painting(message):
    mess = "Лист курсов\n" \
           "1. Как рисовать в фотошопе. Урок для начинающих. - /paintinglesson1 \n" \
           "2. Как нарисовать портрет в технике от пятна. - /paintinglesson2 \n" \
           "3. Как рисовать волосы на графическом планшете. Простые советы - /paintinglesson3 \n" \
           "4. Как БЫСТРЕЕ научиться рисовать на графическом планшете. - /paintinglesson4 \n" \
           "5. Как рисовать в Krita. Самый полный урок для начинающих! - /paintinglesson5 \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["Design"])
def Design(message):
    mess = "Лист курсов\n" \
           "1. Урок 01 UX/UI Design, теория: Введение в UX/UI Design. - /designlesson1 \n" \
           "2. Урок 02 UX/UI Design, теория: Виды сайтов, User Flow - /designlesson2 \n" \
           "3. Урок 03 UX/UI Design, теория: Usability - /designlesson3 \n" \
           "4. Урок 04 UX/UI Design, теория: Wireframes - /designlesson4 \n" \
           "5. Урок 05 UX/UI Design, теория: Подготовка к UI - /designlesson5 \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["designlesson1"])
def getPaint1(message):
    mess = f"Урок 01 UX/UI Design, теория: Введение в UX/UI Design: https://youtu.be/VtH0Kxb_C1I"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["designlesson2"])
def getPaint2(message):
    mess = f"Урок 02 UX/UI Design, теория: Виды сайтов, User Flow: https://youtu.be/CU_SZ5LNZBA"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["designlesson3"])
def getPaint3(message):
    mess = f"Урок 03 UX/UI Design, теория: Usability: hhttps://youtu.be/COLpHd9lt9U"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["designlesson4"])
def getPaint4(message):
    mess = f"Урок 04 UX/UI Design, теория: Wireframes: https://youtu.be/xkoEREo6W3U"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["designlesson5"])
def getPaint5(message):
    mess = f"Урок 05 UX/UI Design, теория: Подготовка к UI: https://youtu.be/vCTsAhdc1Fw"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["paintinglesson1"])
def getPaint1(message):
    mess = f"Как рисовать в фотошопе. Урок для начинающих: https://youtu.be/DtLI4ckvGEI"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["paintinglesson2"])
def getPaint2(message):
    mess = f"Как нарисовать портрет в технике от пятна: https://youtu.be/ihxECo6G514"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["paintinglesson3"])
def getPaint3(message):
    mess = f"Как рисовать волосы на графическом планшете. Простые советы: hhttps://youtu.be/COLpHd9lt9U"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["paintinglesson4"])
def getPaint4(message):
    mess = f"Как БЫСТРЕЕ научиться рисовать на графическом планшете: https://youtu.be/4sdePjEYlis"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["paintinglesson5"])
def getPaint5(message):
    mess = f"Как рисовать в Krita. Самый полный урок для начинающих!: https://youtu.be/l7dcdhE-2KE"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["js"])
def getJs(message):
    mess = f"Курс по JavaScript: https://youtu.be/CxgOKJh4zWE"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["c#"])
def getC(message):
    mess = f"Курс по C#: https://www.youtube.com/watch?v=w8rRhAup4kg"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["c++"])
def getC2(message):
    mess = f"Курс по C++: https://www.youtube.com/watch?v=pwUNLjgw7lY&list=PLQOaTSbfxUtCrKs0nicOg2npJQYSPGO9r&index=6"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["react"])
def getReact(message):
    mess = f"Курс по React/TypeScript: https://youtu.be/GNrdg3PzpJQ"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["python"])
def getPython(message):
    mess = f"Курс по Python: https://youtu.be/cr_3evPrzsU"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["videolesson1"])
def getVideo1(message):
    mess = f"Склейка и обрезка видео: https://youtu.be/BQ3IQfRDVds"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["videolesson2"])
def getVideo2(message):
    mess = f"Кадр: https://www.youtube.com/watch?v=2F8oI-Y1u98"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["videolesson3"])
def getVideo3(message):
    mess = f"DaVinci Resolve 17 для НОВИЧКОВ: https://youtu.be/aaYDUGZJPX8"
    bot.send_message(message.chat.id, mess, parse_mode="html")

# @bot.message_handler(commands=['practice'])
# def getPractice(message):
# 	doc1 = open("./media/template2.docx","rb")
# 	doc2 = open("./media/template1.docx","rb")
# 	doc3 = open("./media/template3.doc","rb")
# 	image1 = open("./media/temp1.png","rb")
# 	image2 = open("./media/temp3.png","rb")

# 	bot.send_document(message.chat.id,doc1)
# 	bot.send_document(message.chat.id,doc2)
# 	bot.send_document(message.chat.id,doc3)
# 	bot.send_photo(message.chat.id, image1)
# 	bot.send_photo(message.chat.id, image2)

@bot.message_handler(commands=["videolesson4"])
def getVideo4(message):
    mess = f"Монтаж в DaVinci Resolve: https://youtu.be/rjBdMeMJHi4"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["videolesson5"])
def getVideo5(message):
    mess = f"Курс по Davinci Resolve: https://youtu.be/WipWScnq3W8"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["photolesson1"])
def getPhoto1(message):
    mess = f"Обработка в Lightroom за 15 МИНУТ: https://youtu.be/OS-Sr7GCkXM"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["photolesson2"])
def getPhoto2(message):
    mess = f"Ретушь кожи в photoshop: https://youtu.be/3ceFVf1ai4c"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["photolesson3"])
def getPhoto3(message):
    mess = f"LIGHTROOM для начинающих: https://youtu.be/eKHaaTJlXXA"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["photolesson4"])
def getPhoto4(message):
    mess = f"Обработка фото в Lightroom / Курс Лайтрум от А до Я: https://youtu.be/uiYnROuRgIQ"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["photolesson5"])
def getPhoto5(message):
    mess = f"Обработка фото в Lightroom / Курс Лайтрум от А до Я/ Часть 2: https://youtu.be/LH5zO1VxIG4"
    bot.send_message(message.chat.id, mess, parse_mode="html")

# @bot.message_handler()
# def explicitContent(message):
#     if message.text == "Hello" or message.text == "hello" or message.text == "Hi" or message.text == "hi":
#         mess = "Hi)\n" \
#                "Use the command /help\n" \
#                "To see the list of commands)"
#         bot.send_message(message.chat.id, mess, parse_mode="html")
#     else:
#         mess = "Sorry, i don't understand you!"
#         bot.send_message(message.chat.id, mess, parse_mode="html")

bot.polling(none_stop=True)


print("Bot stopped")