import telebot;
bot = telebot.TeleBot('%5283548437:AAExvrduO-2FzkPKoDTGWjY1yq9c_XgrKS4%');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, присылай фото")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
	


