import re
from datetime import date, timedelta
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import os

# menghapus stopword
def Stopword(x):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    a = stopword.remove(x)
    return a

# menjadikan array dari file
def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() 
        fileObj.close()
        return words

listOfDeadlines = readFile('../test/deadline.txt')
listOfDeadlinesComponent = []
for i in listOfDeadlines:
        listOfDeadlinesComponent.append(i.split(" "))
katapenting=readFile('../test/katapenting.txt')
keyword_perintah=readFile('../test/keyword_perintah.txt')
keywordss=readFile('../test/keywords.txt')

# date jadi sistem
def convert(today_date):
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
    today_dateConverted= tanggal + " " + bulan + " " + tahun
    return today_dateConverted

def deadlineFromNow(N): 
    Enddate = date.today() + timedelta(days=N)
    tanggalYangDicari = convert(Enddate)
    deadline=""
    for i in listOfDeadlinesComponent:
        if(i[1] + " " + i[2] + " " + i[3]==tanggalYangDicari):
            return deadline+str(i)

def cariKomponenTahun(date) :
    return date[6]+date[7]+date[8]+date[9]

def cariKomponenBulan(date) :
    return date[3] +date[4]

def cariKomponenHari(date) :
    return date[0]+date[1]

def deadlinesBetween(listOfDeadlines,date1,date2):
        date1=readDate(date1)
        date2=readDate(date2)
        start_date = date(int(cariKomponenTahun(date1)),int(cariKomponenBulan(date1)), int(cariKomponenHari(date1)))   
        end_date = date(int(cariKomponenTahun(date2)), int(cariKomponenBulan(date2)), int(cariKomponenHari(date2)))   
        delta = end_date-start_date       
        the_days = []
        for i in range(delta.days + 1):
                day_range = start_date + timedelta(days=i)
                the_days.append(convert(str(day_range)))
        deadlinesSemuanya=""
        for i in listOfDeadlinesComponent:
            for j in the_days:
                if(i[1] + " " + i[2] + " " + i[3]==j):
                    deadlinesSemuanya=deadlinesSemuanya + str(i) + "\n"       
        return deadlinesSemuanya  

def readAdaBerapaTanggal(input):
    pattern = re.compile("[0-9]+(\s|/|-)+(((januari|februari|maret|april|mei|juni|juli|agustus|september|november|desember))|[0-9])+(\s|/|-)+[0-9]+[0-9]",re.IGNORECASE)
    zTotal = re.finditer(pattern,input)
    tanggal=[]
    for x in re.finditer(pattern,input):
        tanggal.append((x.group()))
    return tanggal

def computefail(pattern):
    panjangpattern = len(pattern)
    fail = [0 for i in range (panjangpattern)]
    j = 0
    i = 0

    while(i<panjangpattern):
        if(pattern[j]==pattern[i]):
            fail[i] = j+1
            i+=1
            j+=1
        elif(j>0):
            j = fail[j-1]
        else:
            fail[i]=0
            i+=1

    return fail

def kmpstringmatching(contohstring,contohtext):
    
    panjangstring = len(contohstring)
    panjangtext = len(contohtext)

    fail = computefail(contohtext)

    i = 0
    j = 0

    match = False

    while(match == False and i<panjangstring):
            if(contohtext[j] == contohstring[i]):
                if(j == panjangtext - 1):
                    match = True
                i+=1
                j+=1
            elif(j >0):
                j = fail[j-1]
            else:
                i+=1
    return(match)

def month_string_to_number(string):
    m = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr':'04',
         'mei':'05',
         'jun':'06',
         'jul':'07',
         'agu':'08',
         'sep':'09',
         'okt':'10',
         'nov':'11',
         'des':'12'
        }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

def prosesTanggal(tanggal):
    tanggalDisimpan = tanggal[0]
    if(re.match(re.compile("\d"),tanggal[1])):
        tanggalDisimpan = tanggalDisimpan + tanggal[1]
    if(len(tanggalDisimpan)==1):
        tanggalDisimpan = '0' + tanggalDisimpan
        tanggal = '0' + tanggal
    if(re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[2]) or (re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[3]))):
        if(re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[2])):
            i = 2
        else:
            if (re.match(re.compile("[A-Z]",re.IGNORECASE),tanggal[3])):
                i = 3
        bulan = (month_string_to_number(tanggal[i]+tanggal[i+1]+(tanggal[i+2])))
        print(bulan)
        postString = tanggal.split(" ",3)[2]
        tahun = ""
        for x in re.finditer(re.compile("\d"),postString):
            tahun=tahun+((x.group())) 
    else:   
        postString = tanggal.split(tanggalDisimpan,2)[1]
        bulanTahun = postString[1:]
        bulan = ""
        i=0
        while(re.match(re.compile("\d"),bulanTahun[i])):
            bulan = bulan+bulanTahun[i]
            i=i+1
        if(len(bulan)==1):
            bulan = "0"+bulan
            bulanTahun = "0"+bulanTahun
        tahun=bulanTahun.split(bulan,2)[1][1:]
    if(len(tahun)==2): # tidak ada awalan 20
        tahun = "20" + tahun
    return str(tanggalDisimpan) + " " + str(bulan) + " " + str(tahun)

def readDate(input):
    pattern = re.compile("[0-9]+(\s|/|-)+(((januari|februari|maret|april|mei|juni|juli|agustus|september|november|desember))|[0-9])+(\s|/|-)+[0-9]+[0-9]",re.IGNORECASE)
    zTotal = re.finditer(pattern,input)
    tanggal=[]
    for x in re.finditer(pattern,input):
        tanggal.append((x.group()))
    if(len(tanggal)>0):
        return prosesTanggal(tanggal[0])
    else:
        return None

def deteksiKodeKuliah(input):
    z = re.findall(re.compile("[a-z|A-Z]+[a-z|A-Z]+[0-9]+[0-9]+[0-9]+[0-9]"),input)
    if(len(z)>0):
        return z[0]
    else:
        return None

# menambahkan task baru
def addTask(ID, tanggal,kode,jenis,topik):
    tanggal = tanggal.split(" ")
    data_deadline = []
    data_deadline.append((str(ID) + " "+ str(tanggal[0]) + " " + str(tanggal[1]) + " " + str(tanggal[2]) + " " + str(kode) + " " + str(jenis) + " " + str(topik)))
    listOfDeadlinesComponent.append(data_deadline)
    return "Berhasil menambahkan task"

def tampilkanSeluruhDeadline():
    deadline = ""
    for i in listOfDeadlinesComponent:
        #print(i)
        deadline=deadline + str(i) + "\n"
    return deadline
    
# kata penting
def tampilkanDeadlines(input):
        arraystring = input.split(' ')
        minggu = False
        hari = False
        for i in arraystring:
            if(i=="minggu" or i=="hari"):
                if(kmpstringmatching(i,"minggu")):
                    z=re.findall(re.compile("[0-9]+\s+minggu"),input)
                    if(len(z)>0):
                        banyakminggu=re.match(re.compile("[0-9]"),z[0]).group() # cari angka numerik
                        minggu = True
                        break
                elif(kmpstringmatching(i,"hari")):
                    z=re.findall(re.compile("[0-9]+\s+hari"),input)
                    if(len(z)>0):
                        banyakhari=re.match(re.compile("[0-9]"),z[0]).group() # cari angka numerik
                        hari = True
                        break
        if (readDate(input)==None and minggu==False and hari==False): # kalo misalnya ga ada tanggal
            if(deteksiKataPenting(input)==None):
                return tampilkanSeluruhDeadline()
            else:
                return deadlineKataPenting(input)
        else:
            if(len(readAdaBerapaTanggal(input))==2):
                x=readAdaBerapaTanggal(input)
                return deadlinesBetween(listOfDeadlines,x[0],x[1])
            else:
                if (minggu):
                   if(banyakminggu!=None):
                       return deadlineFromNow(int(banyakminggu)*7)
                elif (hari):
                   if(banyakhari!=None):
                       return deadlineFromNow(int(banyakhari))
                else:
                    output=""
                    for i in listOfDeadlinesComponent:
                        y=readDate(input)
                        x=readAdaBerapaTanggal(y)
                        if(str(i[1])+" "+str(i[2])+" "+str(i[3]) in x):
                            return output + str(i)
        return "Pesan gagal diproses"

# Menampilkan deadline suatu task
def tanyakanDeadline(IDdicari):
    #print(tugas)
    for i in listOfDeadlinesComponent:
        if(i[0].lower()==IDdicari):
            return (i[1]+" "+i[2]+" "+i[3])

# Memperbaharui task tertentu
def perbaharuiTask(IDdicari,tanggalBaru):
    #print(tanggalBaru)
    tugasAda=False
    tanggalBaru=tanggalBaru.split(" ")
    for i in listOfDeadlinesComponent:
        if(i[0].lower()==IDdicari):
            tugasAda = True
            #print("ada")
            i[1]=tanggalBaru[0]
            i[2]=tanggalBaru[1]
            i[3]=tanggalBaru[2]
            return "List berhasil diperbaharui"
    return "Pesan gagal"

# Menandai sudah
def deleteTask(IDdicari):
    for i in listOfDeadlinesComponent:
        if(i[0].lower()==IDdicari):
            listOfDeadlinesComponent.remove(i) # ? wkwk tergantung datanya
            return "List berhasil diperbaharui"
    return "Pesan gagal"

# Menampilkan opsi help
def help():
    output=""
    katapentingstr = ""
    listfitur = " 1. Menambahkan task baru [#katakunci] \r\n 2. Melihat daftar task yang harus dikerjakan [#katakunci] \r\n 3. Menampilkan deadline dari suatu task tertentu [#katakunci]\r\n 4. Memperbaharui task tertentu [#katakunci]\r\n 5. Menandai suatu task sudah selesai [#katakunci] \r\n 6. Menampilkan opsi help [katakunci]\r\n "
    for i in katapenting:
        katapentingstr = katapentingstr + str(i) + "\r\n"
    output="[Fitur] " + "\r\n" + listfitur + "\r\n" + "[Daftar kata penting] " + "\r\n" + katapentingstr
    return output

def deteksiKataPenting(input):
    arraystring = input.split(' ')
    jenis=None
    for j in arraystring:
        if j in katapenting:
            jenis=j
    return jenis

def deadlineKataPenting(input):
    katapenting = deteksiKataPenting(input)
    arrayOfDeadline=[]
    for i in listOfDeadlinesComponent:
        if(i[5].lower()==katapenting):
            arrayOfDeadline.append(i)
    return arrayOfDeadline

def deteksiPerintah(input):
    arraystring = input.split(' ')
    valid=False
    for j in arraystring:
        if j in keyword_perintah:
            valid=True
            return valid
    return valid

def deteksiKeywords(input):
    arraystringg = input.split(' ')
    keyword=None
    for j in arraystringg:
        if j in keywordss:
            keyword=j
    return keyword

def carikmpgak(input,sesuatu):
    arraystring = input.split(' ')
    jenis=False
    for j in arraystring:
        #print(j)
        #print(sesuatu)
        if(kmpstringmatching(j,sesuatu)):
            jenis=True
            break
    return jenis

def pilihanInput(input): # Masuk ke fitur sesuai masukan pengguna
    input = Stopword(input)
    input = input.lower()
    arraystring=input.split(' ')
    tanggal = False
    IDdibaca=False
    kode=False
    returnValue=""
    for i in arraystring:
        if readDate(i)!=None:
            tanggal=True
            tanggalDibaca=readDate(i)
        if deteksiKodeKuliah(i)!=None:
            kode=True
            kodeDibaca=i
        pattern = re.compile("l[0-9][0-9][0-9][0-9]")
        if len(re.findall(pattern,input))>0:
            IDdibaca = True
            IDdicari = re.findall(pattern,input)[0]
    if (deteksiPerintah(input)==False):
        if (kode==True and deteksiKataPenting(input)!=None and deteksiKeywords(input)!=None and tanggal==True):
            if(len(listOfDeadlinesComponent)>=10):
                if(len(listOfDeadlinesComponent)>=100):
                    if(len(listOfDeadlinesComponent)>=1000):
                        ID="L"+str(len(listOfDeadlinesComponent)+1)
                    else:
                        ID="L0"+str(len(listOfDeadlinesComponent)+1)
                else:
                    ID="L00"+str(len(listOfDeadlinesComponent)+1)
            else:
                ID="L000"+str(len(listOfDeadlinesComponent)+1)
            tanggal=tanggalDibaca
            kode=kodeDibaca
            kataPenting=deteksiKataPenting(input)
            topik=deteksiKeywords(input)
            return (addTask(ID, tanggal,kode,kataPenting,topik))
        else:
            return "Maaf, pesan tidak dikenali"
    else: 
        if(kode!=True and carikmpgak(input,"fitur")):
           return help()
        elif((IDdibaca!=True or kode!=True) and carikmpgak(input,"tampilkan")):
            return tampilkanDeadlines(input)
        elif(IDdibaca==True and carikmpgak(input,"kapan")):
            return tanyakanDeadline(IDdicari)
        elif(IDdibaca==True and tanggal==True and carikmpgak(input,"diundur")):
            tanggalBaru = tanggalDibaca
            return perbaharuiTask(IDdicari,tanggalBaru)
        elif(IDdibaca==True and carikmpgak(input,"selesai")):
            return deleteTask(IDdicari)
    return "GAGAL"

def saveDeadlinesComponent():
    # updating ID
    data = listOfDeadlinesComponent
    '''
    j=1
    for i in data:
        if(j>=10):
            if(j>=100):
                if(j>=1000):
                    i[0][0].replace(i[0][0],"D"+str(j))
                else:
                    i[0][0].replace(i[0][0],"D0"+str(j))
            else:
                i[0][0].replace(i[0][0],"D00"+str(j))
        else:
            i[0][0].replace(i[0][0],"D000"+str(j))
        j=j+1
    '''
    with open("../test/deadline.txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line) + "\n")

#print(pilihanInput('tampilkan'))