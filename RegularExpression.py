import re 
from datetime import date, datetime
from calendar import monthrange

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
    ## 15/04/2021 atau 15-04-2021
    ## 14 April 2021
    ## 22/04/21 atau 22-04-2021
    #print(input)
    pattern = re.compile("[0-9]+(\s|/|-)+(((januari|februari|maret|april|mei|juni|juli|agustus|september|november|desember))|[0-9])+(\s|/|-)+[0-9]+[0-9]",re.IGNORECASE)
    zTotal = re.finditer(pattern,input)
    tanggal=[]
    for x in re.finditer(pattern,input):
        tanggal.append((x.group()))
    for i in tanggal:
        print(i)
    if(len(tanggal)>0):
        prosesTanggal(tanggal[0])
    else:
        print("Tidak ada tanggal terdeteksi\n")
    # kalo len tanggal 2, artinya harus cari deadline antara 2 tanggal, artinya diproses juga tanggal[1], wkwk.

# ini sebenernya bisa aja dipisah jadi 3 fungsi buat ngembaliin tanggal, bulan, dan tahun
def prosesTanggal(tanggal):
    tanggalDisimpan = tanggal[0]
    if(re.match(re.compile("\d"),tanggal[1])):
        tanggalDisimpan = tanggalDisimpan + tanggal[1]
    # TANGGAL = tanggalDisimpan
    # print(tanggalDisimpan)
    # buat yang dalam huruf
    if(re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[2]) or (re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[3]))):
        if(re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[2])):
            i = 2
        else:
            if (re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[3])):
                i = 3
        #print(tanggal[i]+tanggal[i+1]+tanggal[i+2])
        bulan = (month_string_to_number(tanggal[i]+tanggal[i+1]+(tanggal[i+2]))) # DAPAT BULANNYA
        #print(bulan)
        postString = tanggal.split(" ",3)[2] # Asumsi kalau menggunakan format bulan dengan huruf, hanya pake " "
        tahun = ""
        for x in re.finditer(re.compile("\d"),postString):
            tahun=tahun+((x.group())) # DAPAT TAHUNNYA
        #print(tahun,"Ini tahun")
    else:   
        postString = tanggal.split(tanggalDisimpan,2)[1]
        bulanTahun = postString[1:]
        print(bulanTahun)
        bulan = ""
        i=0
        while(re.match(re.compile("\d"),bulanTahun[i])):
            bulan = bulan+bulanTahun[i]
            i=i+1
        if(bulan[0]=="0"): # kalo misal ada 0, ignore aja
            bulan=bulan[1:]
        print(bulan)
        tahun=bulanTahun.split(bulan,2)[1][1:]
        print(tahun)
    if(len(tahun)==2): # tidak ada awalan 20
        tahun = "20" + tahun
    '''
    # buat nyimpen deadline dalam bentuk tanggal, bulan, tahun
    deadline = {}
    deadline[date]=tanggalDisimpan
    deadline[month]=bulan
    deadline[year]=tahun
    return deadline
    '''

def cariBerapaMingguAtauHari(input):
    if(kmpstringmatching(input,"minggu")):
        z=re.match(re.compile("[0-9]+\s+minggu"),input)
        x=re.match(re.compile("[0-9]"),z.group()) # cari angka numerik
        print(x) # artinya x minggu
    elif(kmpstringmatching(input,"hari")):
        z=re.match(re.compile("[0-9]+\s+hari"),input)
        x=re.match(re.compile("[0-9]"),z.group()) # cari angka numerik
        print(x) # artinya x hari
    return x

#input = input("Masukkan input: ")
#cariBerapaMingguAtauHari(input)

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

def main():
    perintah=""
    while(perintah!="exit"):
        perintah = input("Masukkan sesuatu: ")
        readDate(perintah)
        perintah = input("Tulis exit untuk keluar:")

# def isDeadlineValid(deadline): # buat ngecek tanggal terakhir bulannya bener ga, males tp nanti aja haha

'''
# periode waktu tertentu

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

# deadline bbrp hari/minggu ke depan
def deadlineFromNow(N): # N hari kedepan # N minggu kedepan * 7
    return listOfDeadlines[today+N]

# deadline hari ini
def deadlineToday():
    return listOfDeadlines[today]

'''

#main()
