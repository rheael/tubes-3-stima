import re

#from RegularExpression import *
#from kmpstringmatching import *

# BARU GAMBARAN
# Harus diintegrasikan sama penyimpanan data

def deadlineFromNow(N): # N hari kedepan # N minggu kedepan * 7
    #return listOfDeadlines[today+N]
    return True

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

def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() 
        fileObj.close()
        return words

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
        #print(bulanTahun)
        bulan = ""
        i=0
        while(re.match(re.compile("\d"),bulanTahun[i])):
            bulan = bulan+bulanTahun[i]
            i=i+1
        if(bulan[0]=="0"): # kalo misal ada 0, ignore aja
            bulan=bulan[1:]
        #print(bulan)
        tahun=bulanTahun.split(bulan,2)[1][1:]
        #print(tahun)
    if(len(tahun)==2): # tidak ada awalan 20
        tahun = "20" + tahun
    return str(tanggalDisimpan) + "/" + str(bulan) + "/" + str(tahun)
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
        x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
        print(x) # artinya x minggu
    elif(kmpstringmatching(input,"hari")):
        z=re.match(re.compile("[0-9]+\s+hari"),input)
        x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
        print(x) # artinya x hari
    return x

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


listOfDeadlines = readFile('deadline.txt')
listOfDeadlinesComponent = []
for i in listOfDeadlines:
        listOfDeadlinesComponent.append(i.split(" "))

def deteksiKodeKuliah(input):
    z = re.findall(re.compile("[A-Z]+[A-Z]+[0-9]+[0-9]+[0-9]+[0-9]"),input)
    if(len(z)>0):
        return z[0]
    else:
        return None

#print(deteksiKodeKuliah("Aku benci IF2230"))

# Menambahkan task baru
def addTask(tanggal,kode,jenis,topik):
    data_deadline = (str(tanggal) + " " + str(kode) + " " + str(jenis) + " " + str(topik) + "\n")
    with open('tugas.txt', 'a+') as f:
        f.write(data_deadline)

def tampilkanSeluruhDeadline():
    for i in listOfDeadlines:
        print(i)
    
def tampilkanDeadlines(input):
        if readDate(input)!=None: # kalo misalnya ga ada tanggal
            tampilkanSeluruhDeadline()
        else:
            if(len(readAdaBerapaTanggal(input))==2):
                x=readAdaBerapaTanggal()
                deadlinesBetween(listOfDeadlines,x[0],x[1])
            else:
                if (kmpstringmatching(input,"minggu")):
                   jumlahMinggu = cariBerapaMingguAtauHari(input)
                   deadlineFromNow(jumlahMinggu*7)
                elif (kmpstringmatching(input,"hari")):
                   jumlahHari = cariBerapaMingguAtauHari(input)
                   deadlineFromNow(jumlahHari)

def cariBerapaMingguAtauHari(input):
    if(kmpstringmatching(input,"minggu")):
        z=re.match(re.compile("[0-9]+\s+minggu"),input)
        if(z!=None):
            x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
        else:
            return None
        print(x) # artinya x minggu
    elif(kmpstringmatching(input,"hari")):
        z=re.match(re.compile("[0-9]+\s+hari"),input)
        if(z!=None):
            x=re.match(re.compile("[0-9]"),z.group()).group() # cari angka numerik
        else:
            return None
        print(x) # artinya x hari
    return x

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
                return listOfDeadlines[i]
    
# Berdasarkan jenis task
# cari tanggal/waktu (contoh: 3 minggu, 3 hari)
 # artinya kata penting lagi minggu sama hari
# yuuk dihitung minggu itu berapa, hari itu berapa:)

# Menampilkan deadline suatu task
def tanyakanDeadline(tugas):
    #print(tugas)
    for i in listOfDeadlinesComponent:
        if (i[1]==tugas):
            return i[0]

# tanggal Deadline sesuai penyimpanan

# Memperbaharui task tertentu
def perbaharuiTask(tugas,tanggalBaru):
    tugasAda=False
    for i in listOfDeadlinesComponent:
        if(i[1]==tugas):
            tugasAda = True
            i[0]=tanggalBaru
            break

# Menandai sudah
def deleteTask(tugas):
    for i in listOfDeadlinesComponent:
        if(i[1]==tugas):
            listOfDeadlinesComponent.remove(i) # ? wkwk tergantung datanya
            break

# Menampilkan opsi help
def help():
    print("Fitur") #dst
    print("Daftar kata penting")

def deteksiKataPenting(input):
    katapenting=readFile('katapenting.txt')
    jenis=None
    for i in katapenting:
        if(kmpstringmatching(input,i)):
            jenis=i
            break
    return jenis

def pilihanInput(input): # Masuk ke fitur sesuai masukan pengguna
    # harus ada topik, harus ada selain stopwords
    if (readDate(input)!=None and deteksiKodeKuliah(input)!=None and deteksiKataPenting(input)!=None and kmpstringmatching("aku","aku")==False):
        addTask(readDate(input), deteksiKodeKuliah(input), deteksiKataPenting(input), "hoho")
    else:
        #tugas = deteksiKodeKuliah(input)
        #print(tugas)
        #tampilkanDeadlines(input)
        for i in listOfDeadlinesComponent:
            print(i)
        if(kmpstringmatching(input,"kapan")):
            tugas = deteksiKodeKuliah(input)
            print(tanyakanDeadline(tugas))
        elif(kmpstringmatching(input,"diundur")):
            tanggalBaru = readDate(input)
            tugas = deteksiKodeKuliah(input)
            perbaharuiTask(tugas,tanggalBaru)
        elif(kmpstringmatching(input,"selesai")):
            tugas = deteksiKodeKuliah(input)
            deleteTask(tugas)
        elif(kmpstringmatching(input,"bantuan")):
            help()
        elif(kmpstringmatching(input,"tampilkan")):
            tampilkanDeadlines(input)
        else:
            print("Maaf, pesan tidak dikenali\n")
    print(listOfDeadlinesComponent)


input = input("Masukkan input: ")
pilihanInput(input)