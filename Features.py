import re
from datetime import date, timedelta
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import StopWordRemoverFactory class
# import Sastrawi package
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#from RegularExpression import *
#from kmpstringmatching import *

# BARU GAMBARAN
# Harus diintegrasikan sama penyimpanan data

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

'''
# bikin jadi kata dasar
def Stem(x):
    a = stemmer.stem(x)
    return a
    # bikin keluar "none"
'''

# ngilangin kata kata ga penting
def Stopword(x):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    a = stopword.remove(x)
    return a

# ngegabungin
def Simplify(x):
    a = Stopword(x)
    b = Stem(a)
    return b

def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() 
        fileObj.close()
        return words

listOfDeadlines = readFile('deadline.txt')
listOfDeadlinesComponent = []
for i in listOfDeadlines:
        listOfDeadlinesComponent.append(i.split(" "))

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
    today_dateConverted= tanggal + " " + bulan + " " + tahun
    return today_dateConverted

def deadlineFromNow(N): # N hari kedepan # N minggu kedepan * 7
    #return listOfDeadlines[today+N]
    Enddate = date.today() + timedelta(days=N)
    tanggalYangDicari = convert(Enddate)
    deadline=""
    for i in listOfDeadlinesComponent:
        if(i[0] + " " + i[1] + " " + i[2]==tanggalYangDicari):
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
                if(i[0] + " " + i[1] + " " + i[2]==j):
                    #print(j)
                    deadlinesSemuanya=deadlinesSemuanya + (i) + "\n"
                             
        return deadlinesSemuanya  

#print(deadlinesBetween(listOfDeadlinesComponent,'27 04 2020','27 05 2020'))

def readAdaBerapaTanggal(input):
    pattern = re.compile("[0-9]+(\s|/|-)+(((januari|februari|maret|april|mei|juni|juli|agustus|september|november|desember))|[0-9])+(\s|/|-)+[0-9]+[0-9]",re.IGNORECASE)
    zTotal = re.finditer(pattern,input)
    tanggal=[]
    for x in re.finditer(pattern,input):
        tanggal.append((x.group()))
    return tanggal

#readAdaBerapaTanggal("27/04/2020")

#print(readAdaBerapaTanggal('27/04/2020'))

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
        #while(i<panjangstring):
            if(contohtext[j] == contohstring[i]):
                if(j == panjangtext - 1):
                    #print(i - panjangtext + 1)
                    match = True
                    #print("match found")
                i+=1
                j+=1
            elif(j >0):
                j = fail[j-1]
                #print("disini1")
            else:
                i+=1
                #print("disini2")

    #if(match == True):
    #    print("ketemu :3")
    #else:
    #    print("nothing here")
    return(match)
    
    #return True

def month_string_to_number(string):
    #print(string)
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


# ini sebenernya bisa aja dipisah jadi 3 fungsi buat ngembaliin tanggal, bulan, dan tahun
def prosesTanggal(tanggal):
    tanggalDisimpan = tanggal[0]
    if(re.match(re.compile("\d"),tanggal[1])):
        tanggalDisimpan = tanggalDisimpan + tanggal[1]
    if(len(tanggalDisimpan)==1):
        tanggalDisimpan = '0' + tanggalDisimpan
        tanggal = '0' + tanggal
    #print(tanggalDisimpan)
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
        print(bulan)
        postString = tanggal.split(" ",3)[2] # Asumsi kalau menggunakan format bulan dengan huruf, hanya pake " "
        tahun = ""
        for x in re.finditer(re.compile("\d"),postString):
            tahun=tahun+((x.group())) # DAPAT TAHUNNYA
        #print(tahun,"Ini tahun")
    else:   
        postString = tanggal.split(tanggalDisimpan,2)[1]
        bulanTahun = postString[1:]
        #print(bulanTahun)
        bulan = ""
        i=0
        while(re.match(re.compile("\d"),bulanTahun[i])):
            bulan = bulan+bulanTahun[i]
            i=i+1
        if(len(bulan)==1):
            bulan = "0"+bulan
            bulanTahun = "0"+bulanTahun
        #print(bulan)
        tahun=bulanTahun.split(bulan,2)[1][1:]
        #print(tahun)
    if(len(tahun)==2): # tidak ada awalan 20
        tahun = "20" + tahun
    return str(tanggalDisimpan) + " " + str(bulan) + " " + str(tahun)
    '''
    # buat nyimpen deadline dalam bentuk tanggal, bulan, tahun
    deadline = {}
    deadline[date]=tanggalDisimpan
    deadline[month]=bulan
    deadline[year]=tahun
    return deadline
    '''
#print(prosesTanggal('3 04 2020'))

'''
def cariBerapaMingguAtauHari(input):
    x=None
    arraystring = input.split(' ')
    for i in arraystring:
        if(kmpstringmatching(i,"minggu")):
            z=re.match(re.compile("[0-9]+\s+minggu"),input)
            if(z!=None):
                x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
                return x
        elif(kmpstringmatching(i,"hari")):
            z=re.match(re.compile("[0-9]+\s+hari"),input)
            if(z!=None):
                x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
                return x
    return x
'''

#input = input("Masukkan input: ")
#cariBerapaMingguAtauHari(input)
'''
def main():
    perintah=""
    while(perintah!="exit"):
        perintah = input("Masukkan sesuatu: ")
        readDate(perintah)
        perintah = input("Tulis exit untuk keluar:")
'''

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
        #print(tanggal)
    #for i in tanggal:
        #print(i)
    if(len(tanggal)>0):
        return prosesTanggal(tanggal[0])
    else:
        return None
    #prosesTanggal(tanggal[0])
    #return tanggal
    #else:
    #    print("Tidak ada tanggal terdeteksi\n")
    # kalo len tanggal 2, artinya harus cari deadline antara 2 tanggal, artinya diproses juga tanggal[1], wkwk.

#print(readDate('23 05 2020'))

def deteksiKodeKuliah(input):
    z = re.findall(re.compile("[a-z]+[a-z]+[0-9]+[0-9]+[0-9]+[0-9]"),input)
    if(len(z)>0):
        return z[0]
    else:
        return None

# Menambahkan task baru
def addTask(tanggal,kode,jenis,topik):
    tanggal = tanggal.split(" ")
    data_deadline = (str(tanggal[0]) + " " + str(tanggal[1]) + " " + str(tanggal[2]) + " " + str(kode) + " " + str(jenis) + " " + str(topik) + "\n")
    listOfDeadlinesComponent.append(data_deadline)
    #with open('tugas.txt', 'a+') as f:
    #    f.write(data_deadline)

def tampilkanSeluruhDeadline():
    deadline = ""
    for i in listOfDeadlinesComponent:
        print(i)
        deadline=deadline + str(i) + "\n"
    return deadline
    
def tampilkanDeadlines(input):
        arraystring = input.split(' ')
        minggu = False
        hari = False
        for i in arraystring:
            if(i=="minggu" or i=="hari"):
                if(kmpstringmatching(i,"minggu")):
                    #print(kmpstringmatching(i,"minggu"))
                    z=re.findall(re.compile("[0-9]+\s+minggu"),input)
                    if(len(z)>0):
                        banyakminggu=re.match(re.compile("[0-9]"),z[0]).group() # cari angka numerik
                        minggu = True
                        break
                elif(kmpstringmatching(i,"hari")):
                    #print(kmpstringmatching(i,"hari"))
                    z=re.findall(re.compile("[0-9]+\s+hari"),input)
                    if(len(z)>0):
                        banyakhari=re.match(re.compile("[0-9]"),z[0]).group() # cari angka numerik
                        hari = True
                        break
        if (readDate(input)==None and minggu==False and hari==False): # kalo misalnya ga ada tanggal
            return tampilkanSeluruhDeadline()
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
                        if(i[0]+" "+i[1]+" "+i[2] in x):
                            return output + str(i)
        return "Pesan gagal diproses"


# Menampilkan deadline suatu task
def tanyakanDeadline(tugas):
    #print(tugas)
    for i in listOfDeadlinesComponent:
        if(i[3].lower()==tugas):
            return (i[0]+" "+i[1]+" "+i[2])

# tanggal Deadline sesuai penyimpanan

# Memperbaharui task tertentu
def perbaharuiTask(tugas,tanggalBaru):
    #print(tanggalBaru)
    tugasAda=False
    tanggalBaru=tanggalBaru.split(" ")
    for i in listOfDeadlinesComponent:
        if(i[3].lower()==tugas):
            tugasAda = True
            #print("ada")
            i[0]=tanggalBaru[0]
            i[1]=tanggalBaru[1]
            i[2]=tanggalBaru[2]
            return "List berhasil diperbaharui"
    return "Pesan gagal"

# Menandai sudah
def deleteTask(tugas):
    for i in listOfDeadlinesComponent:
        if(i[3].lower()==tugas):
            listOfDeadlinesComponent.remove(i) # ? wkwk tergantung datanya
            return "List berhasil diperbaharui"
    return "Pesan gagal"

# Menampilkan opsi help
def help():
    output=""
    output="Fitur"+"\n"+"Daftar kata penting"

katapenting=readFile('katapenting.txt')
def deteksiKataPenting(input):
    #katapenting=readFile('katapenting.txt')
    #contohstring = "aku mau mau mau mau banget tucil"
    arraystring = input.split(' ')
    jenis=None
    for j in arraystring:
        if j in katapenting:
            jenis=j
    return jenis

keyword_perintah=readFile('keyword_perintah.txt')
def deteksiPerintah(input):
    arraystring = input.split(' ')
    valid=False
    for j in arraystring:
        if j in keyword_perintah:
            valid=True
            return valid
    return valid

def deteksiKeywords(input):
    keywordss=readFile('keywords.txt')
    arraystringg = input.split(' ')
    keyword=None
    for j in arraystringg:
        if j in keywordss:
            keyword=j
    return keyword

def carikmpgak(input,sesuatu):
    #katapenting=readFile('katapenting.txt')
    #contohstring = "aku mau mau mau mau banget tucil"
    arraystring = input.split(' ')
    #print(arraystring)

    #print(arraystring)
    #contohtext = "tucil"
    jenis=False
    
    for j in arraystring:
        #print(j)
        #print(sesuatu)
        if(kmpstringmatching(j,sesuatu)):
            jenis=True
            break
    return jenis

#print(carikmpgak('sesuatu','sesuatu'))

def pilihanInput(input): # Masuk ke fitur sesuai masukan pengguna
    input = Stopword(input)
    #print(input)
    # harus ada topik, harus ada selain stopwords
    #print(deteksiPerintah(input))
    if (deteksiPerintah(input)==False):
        # Gak ada kata perintah, asumsi dia mau nambahin 
        if (readDate(input)!=None and deteksiKodeKuliah(input)!=None and deteksiKataPenting(input)!=None):
            ### TAMBAHKAN TASK
            #input = input.split(readDate(input),2)[1]
            #input = input.split(deteksiKataPenting(input),2)[1]
            #input = input.split(deteksiKodeKuliah(input),2)[1]
            print(input)
            # Asumsi kalau menggunakan format bulan dengan huruf, hanya pake " "
            #addTask(readDate(input), deteksiKodeKuliah(input), deteksiKataPenting(input), "hoho")
        # Kalo gaada tanggal, kode, kata penting, ga dikenali
        else:
            return "Maaf, pesan tidak dikenali"
    else: 
        #tugas = deteksiKodeKuliah(input)
        #print(tugas)
        #tampilkanDeadlines(input)
        #tampilkanDeadlines(input)
        #for i in listOfDeadlinesComponent:
        #    print(i)
        #print(deteksiKodeKuliah)
        if(carikmpgak(input,"bantu")):
            return help()
        elif(carikmpgak(input,"tampil")):
            return tampilkanDeadlines(input)
        elif(deteksiKodeKuliah(input)!=None and carikmpgak(input,"kapan")):
            tugas = deteksiKodeKuliah(input)
            return tanyakanDeadline(tugas)
        elif(deteksiKodeKuliah(input)!=None and carikmpgak(input,"undur") and readDate(input)!=None):
            tanggalBaru = readDate(input)
            tugas = deteksiKodeKuliah(input)
            return perbaharuiTask(tugas,tanggalBaru)
        elif(deteksiKodeKuliah(input)!=None and carikmpgak(input,"selesai")):
            tugas = deteksiKodeKuliah(input)
            return deleteTask(tugas)
           
    print(listOfDeadlinesComponent)
 
def saveDeadlinesComponent() :
    data = listOfDeadlinesComponent
    with open("deadline.txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line) + "\n")

input = input("Masukkan input: ")
pilihanInput(input)
