import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8')

game_active = False
number = None
max_attempts = 3
attempts = 0

@bot.message_handler(commands=['ارقام', 'start'])
def start(message):
    global game_active, attempts
    game_active = False
    attempts = 0

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("ابدأ اللعبة", callback_data="start_game"))
    bot.reply_to(message, 'اهلاً حياك الله! اضغط على الزر لبدء اللعبة.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def start_game(call):
    global game_active, number, attempts
    if not game_active:
        number = random.randint(1, 10)
        bot.reply_to(call.message, 'اختر أي رقم من 1 إلى 10 🌚 ')
        game_active = True
        attempts = 0
    else:
        bot.reply_to(call.message, 'اللعبة قيد التشغيل، يرجى انتهاء الجولة الحالية أولاً.')

@bot.message_handler(func=lambda message: game_active)
def handle_guess(message):
    global game_active, number, attempts
    try:
        guess = int(message.text)
        attempts += 1

        if guess == number:
            bot.reply_to(message, "مُبارك فزتها بفخر 🥳")
            video_url = "https://t.me/VIPABH/2"
            bot.send_video(message.chat.id, video_url)
            game_active = False
        elif attempts >= max_attempts:
            bot.reply_to(message, f"للأسف، لقد نفدت محاولاتك. الرقم الصحيح هو {number}.🌚")
            video_url = "https://t.me/VIPABH/23"
            bot.send_video(message.chat.id, video_url)
            game_active = False
        else:
            bot.reply_to(message, "جرب مرة لخ، الرقم غلط💔")

    except ValueError:
        bot.reply_to(message, "يرجى إدخال رقم صحيح")

bot.polling()
