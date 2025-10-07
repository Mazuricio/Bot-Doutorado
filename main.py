import telebot
#import schedule, time
import time
from sopa import edital_25
import os
from dotenv import load_dotenv
# Carrega as variáveis do arquivo .env

load_dotenv()

# Acessa a variável
token = os.getenv("TELEGRAM_TOKEN")
my_id = os.getenv("MY_ID")
input("aqui")
bot = telebot.TeleBot(token)


print("Bot Online")
bot.send_message(my_id, "Estou online")
def edital():
    print("Enviando Aviso")
    lista25, lista = edital_25()
    print(lista25)
    print(lista)
    if len(lista25) == 0:
        bot.send_message(my_id, (f"Nada chefe, a ultima é: {lista[1]}"))
        print("nada chefe")
    else:
        bot.send_message(my_id, "Saiu chefe, corre lá ver")
        time.sleep(2)
        print(lista25)
        bot.send_message(my_id, lista25[1])

schedule.every().day.at("08:00").do(edital)
#schedule.every().day.at("10:00").do(edital)
schedule.every().day.at("12:00").do(edital)
#schedule.every().day.at("14:00").do(edital)
#schedule.every().day.at("16:08").do(edital)
#schedule.every().day.at("16:00").do(edital)
schedule.every().day.at("18:00").do(edital)
#schedule.every().day.at("20:00").do(edital)

#while True:
#    schedule.run_pending()
#    time.sleep(5)

edital()
