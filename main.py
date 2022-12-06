import telebot
from datetime import datetime
from settings import token, bot_url

bot = telebot.TeleBot(token)

print(f"Bot Started!. Follow the link {bot_url}")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Hello, <b>{message.from_user.first_name}</b>. How can I help you?\n" \
           "View the list of commands: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["help"])
def help(message):
    mess = "Command list\n" \
           "1. Show Time - /time\n" \
           "2. Show Date - /date\n" \
           "3. Show Id - /id\n" \
           "4. Show Toilets - /toilets \n" \
           "5. Call Schedule - /call \n" \
           "6. Get report templates - /practice \n" \
           "7. Сomputer classes - /computers \n" \
           "8. Places to eat - /eat \n" \
           "9. Prices to eat - /eatprice \n" \
           "10. Leave feedback to 2GIS - /map \n" 
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["date"])
def getDate(message):
    _date = datetime.now()
    mess = f"Today: {_date.day}/{_date.month}/{_date.year}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["eat"])
def eatPlaces(message):
    mess = f"The nearest store is on the 4th floor of the INTC college building"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["map"])
def eatPlaces(message):
    mess = f"Leave feedback: https://2gis.kz/almaty/firm/70000001040563276?m=76.915603%2C43.236066%2F16.65"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["eatprice"])
def eatPlaces(message):
    mess = f"Sandwich - 300KZT \nWater - 200KZT\nFuse tea - 300KZT\nSandwich Panini - 500KZT"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["computers"])
def eatPlaces(message):
    mess = f"Computer classes: 405cab, 406cab, 407cab, 409cab, 506cab, 509cab, 609cab, 709cab, 706cab"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["call"])
def getCall(message):
    mess = f"Call Schedule \nFirst shift: \n    First pair - 8:00|9:20 \n    Second pair - 9:30|10:50 \n    Third pair - 11:00|12:20 \n Second shift: \n    First pair - 13:30|14:50 \n    Second pair - 15:00|16:20 \n    Third pair - 16:30|17:50"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["time"])
def getTime(message):
    _time = datetime.now()
    mess = f"Now: {_time.hour}:{_time.minute}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["id"])
def getId(message):
    _id = message.from_user.id
    mess = f"Your id: {_id}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=['practice'])
def getPractice(message):
	doc1 = open("./media/template2.docx","rb")
	doc2 = open("./media/template1.docx","rb")
	doc3 = open("./media/template3.doc","rb")
	image1 = open("./media/temp1.png","rb")
	image2 = open("./media/temp3.png","rb")

	bot.send_document(message.chat.id,doc1)
	bot.send_document(message.chat.id,doc2)
	bot.send_document(message.chat.id,doc3)
	bot.send_photo(message.chat.id, image1)
	bot.send_photo(message.chat.id, image2)

@bot.message_handler(commands=["toilets"])
def getToilets(message):
    mess = f"Men's toilets: \n 4 floor \n 6 floor \n 7 floor \n Women's toilets: \n 3 floor  \n 5 floor"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def explicitContent(message):
    if message.text == "Hello" or message.text == "hello" or message.text == "Hi" or message.text == "hi":
        mess = "Hi)\n" \
               "Use the command /help\n" \
               "To see the list of commands)"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    else:
        mess = "Sorry, i don't understand you!"
        bot.send_message(message.chat.id, mess, parse_mode="html")


bot.polling(none_stop=True)


print("Bot stopped")