from telegram.ext import *
import schedule
import time
import telegram

my_token = '<telegram-bot-token>'

bot = telegram.Bot(token=my_token)

def sayhi():
    bot.send_message(chat_id=1105275553, text="hi")    

def main():
    
    schedule.every(5).seconds.do(sayhi)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()



