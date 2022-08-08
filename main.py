# Created by Miracle Programmer, 08.08.2022

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5510993522:AAE3oVlizERR8NOvtXrH_cyDAMz2C_5PCEY'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f'Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!'
    xabar += '\nMatningizni yuboring.'
    bot.reply_to(message, xabar)

# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))
    
 
bot.polling()