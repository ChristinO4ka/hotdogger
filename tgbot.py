import telebot
from PIL import Image
from telebot import types
import torch
import cv2
import pandas as pd
import yaml
from tqdm import tqdm

bot = telebot.TeleBot('5283548437:AAExvrduO-2FzkPKoDTGWjY1yq9c_XgrKS4');
model = torch.hub.load('ultralytics/yolov5', 'custom', 
	path = r"C:\Users\xpiot\Downloads\best.pt",
	force_reload = True)
@bot.message_handler(content_types=['text', 'photo', 'document'])
def get_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, присылай фото своего хотдога")
	elif message.text == "/help":
	    bot.send_message(message.from_user.id, "Напиши привет")
	elif  message.content_type == 'photo':
		file_info = bot.get_file(message.photo[-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src = message.photo[-1].file_id
		with open('photo.png', 'wb') as new_file:
			new_file.write(downloaded_file)
		img = Image.open(r'C:\Users\xpiot\photo.png')
		results = model(img)
		conf = round(results.pandas().xyxy[0].confidence, 3) * 100
		if conf.empty:
			bot.send_message(message.from_user.id, "Эй, жулик, это не хотдог")
		elif max(conf) <= 0.5:
			bot.send_message(message.from_user.id, "Эй, жулик, это не хотдог")
		else:
			def conv(n): 
			    es = ['а', 'и', '']
			    n = n % 100
			    if n>=11 and n<=19:
			        s=es[2] 
			    else:
			        i = n % 10
			        if i == 1:
			            s = es[0] 
			        elif i in [2,3,4]:
			            s = es[1] 
			        else:
			            s = es[2] 
			    return s 
			bot.send_message(message.from_user.id, f"Это хотдог. {len(conf)} штук{conv(len(conf))}")
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)	

