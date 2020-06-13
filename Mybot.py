import telebot
import mysql.connector
import uchitoken

from datetime import date
from datetime import datetime
TOKEN = uchitoken.TOKEN
myBot= telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper

waktusekarang = datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        teks = uchitoken.SAPA +"\n" + "/start untuk memulai"+"\n" \
               +"/help untuk mengetahui fitur apa saya yang tersedia" +"\n"\
                + "/info untuk mengetahui sejarah tentang bot ini "+"\n"\
               +"/datasiswa untuk melihat data siswa kelas XI RPL 1&2" \
               "\n-- admin & developer @FarisFerdiansyah - SMK Taruna Bhakti -- "+"\n" \
                "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['info'])
    def info(message):
        teks = "Bot ini diciptakan oleh @FarisFerdiansyah ,tujuan diciptakannya bot ini adalah karna sang developer sedang belajar membuat bot untuk melakukan perkerjaan - pekerjaan secara otomatis "
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def help_command(message):
        tulis = "/start untuk memulai bot" + "\n" + "/help untuk melihat apa saja yang bisa dilakukan bot ini" + "\n" + "/datasiswa untuk melihat untuk melihat data siswa kelas XI RPL 1&2"
        myBot.reply_to(message, tulis)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            # print(data)
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '\n')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message, str(kumpuldata))


# print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)