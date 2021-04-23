import re 
from datetime import date, datetime

#today_date = date.today()

#print(str(today_date)) # ini date python

# date.today di python = 2021-04-22
# kalo di sistem bisa dibikin jadi 22/04/2021

# contoh
def convert(today_date):
    # ubah jadi sistem
    tahun = ""
    bulan = ""
    tanggal = ""
    i = 0
    while(i<=3):
        tahun = tahun + str(today_date)[i]
        i=i+1
    i=i+1
    while(i<=6):
        bulan = bulan + str(today_date)[i]
        i=i+1
    i=i+1
    while(i<=9):
        tanggal = tanggal + str(today_date)[i]
        i=i+1
    today_dateConverted= tanggal + "/" + bulan + "/" + tahun
    return today_dateConverted

# print(convert(today_date))

# input = "Apa saja deadline antara 03/04/2021 sampai 15/04/2021?"
# inputLain = "Tubes IF2211 String Matching pada 14 April 2021"
# inputLainLagi = "Halo bot, tolong ingetin kalau ada kuis IF3110 Bab 2 sampai 3 pada 22/04/21"

def readDate(input):
    ## ada 3 pilihan input
    ## 15/04/2021
    ## 14 April 2021
    ## 22/04/21
    print(input)
    pattern = re.compile("[0-9]+(\s|/)+(((januari|februari|maret|april|mei|juni|juli|agustus|september|november|desember))|[0-9])+(\s|/)+[0-9]+[0-9]",re.IGNORECASE)
    zTotal = re.search(pattern,input)
    if(zTotal!=None):
        simpan = (str(zTotal).split("match='"))
        pattern = r"'>"
        simpan = re.sub(pattern,'',simpan[1])
        print(zTotal)
        print(simpan)

def main():
    perintah=""
    while(perintah!="exit"):
        perintah = input("Masukkan sesuatu: ")
        readDate(perintah)
        perintah = input("Tulis exit untuk keluar:")

# print(month_string_to_number("januari"))

'''

sama biar orang bisa nyari deadline antara dua tanggal

def cobaCaraBulan(input):

# PERIODE WAKTU TERTENTU

# N MINGGU KE DEPAN

# N HARI KE DEPAN

# HARI INI

# BIKIN DATA KALENDER !!
# DATES BETWEEN


def bulan(date):
    
def tanggal(date):
    
def lastDateOf(bulan):

def deadlinesBetween(listOfDeadlines,date1,date2):
    if(bulan(date1)==bulan(date2)):
        i = tanggal(date1)
        while(i<tanggal(date2)):
            # return listOfDeadlines[i]
            i=i+1
    else:
        if(bulan(date1)-bulan(date2)>0):
            i = tanggal(date1)
            while(i<lastDateOf(bulan(date1))):
                # return listOfDeadlines[i]
        else:

def deadlineFromNow(N): # N hari kedepan # N minggu kedepan * 7
    return listOfDeadlines[today+N]

def deadlineToday():
    return listOfDeadlines[today]

def isTanggalValid():

'''

main()
