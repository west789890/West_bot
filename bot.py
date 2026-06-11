import telebot
import random
from telebot import types

# Ton token est intégré ici pour faire fonctionner @Fwest_bot
API_TOKEN = '8151607593:AAH_Z7uHAt-jD5nSclS9-qBshLg6wXQvHqI'

bot = telebot.TeleBot(API_TOKEN)

def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎰 Nouvelle prédiction", callback_data="new_pred"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "👋 BIENVENUE SUR WESTBOT LUCKY JET !\n\nClique sur le bouton ci-dessous pour obtenir ton signal.", 
        reply_markup=get_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data == "new_pred")
def callback_new_pred(call):
    cote = round(random.uniform(1.50, 5.00), 2)
    texte = f"🚀 **PRÉDICTION TROUVÉE** 🚀\n\n🎯 Côte : **X{cote}**\n\n✅ _Statut : En cours..._"
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        text=texte,
        parse_mode="Markdown",
        reply_markup=get_keyboard()
    )

bot.polling(none_stop=True)

