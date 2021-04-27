import re

#from RegularExpression import *
#from kmpstringmatching import *

# BARU GAMBARAN
# Harus diintegrasikan sama penyimpanan data

def deteksiKodeKuliah(input):
    z = re.match(re.compile("[A-Z]+[A-Z]+[0-9]+[0-9]+[0-9]+[0-9]"),input)
    print(z)
    return (z.group())

#input = input("Masukkan input: ")
#deteksiKodeKuliah(input)

def pilihanInput(input): # Masuk ke fitur sesuai masukan pengguna
    if(kmpstringmatching(input,"kapan")):
        tugas = deteksiKodeKuliah(input)
        tanyakanDeadline(tugas)
    elif(kmpstringmatching(input,"diundur")):
        tugas = deteksiKodeKuliah(input)
        perbaharuiTask(tugas)
    elif(kmpstringmatching(input,"selesai")):
        tugas = deteksiKodeKuliah(input)
        deleteTask(tugas)
    elif(kmpstringmatching(input,"help")):
        help()
    elif(kmpstringmatching(input,"tampilkan")):
        tampilkanDeadlines()
    else:
        print("Maaf, pesan tidak dikenali\n")

# Menambahkan task baru
def addTask(tanggal,kode,jenis,topik):
    input = input("Masukkan task: " )
    print("[TASK BERHASIL DICATAT]\n")
    print((ID:1) 14/04/2021 - IF2211 - Tubes - String matching)
    ID = len(listOfDeadlines)+1
    tanggal = readDate(input)
    kodematkul = deteksiKodeKuliah(input)
    jenis = re.match(input, "...").group() # semua kata penting
    #topik = semua setelah semua kata penting yang bukan tanggal, bukan stopwords

def tampilkanSeluruhDeadline():
    for i in listOfDeadlines:
        print(i)
    
'''
def tampilkanDeadlines():
        # if gaada tanggal.periode waktu khusus, artinya tampilkan semua
        #    tampilkanSeluruhDeadline()
        # else:
        #    readDate(input)
            # kurang lebih kayak di RegularExpression.py
            # if (len dari array yang dihasilkan lebih dari 2, artinya harus cari antara dua deadline)
            # minggu-hari
            # else:
            #   pake fungsi yang ada di RegularExpression.y
            #    if (kmpstringmatching(input,"minggu"):
            #       jumlahMinggu = cariBerapaMingguAtauHari(input)
            #       deadlineFromNow(jumlahMinggu*7)
            #    elif kmpstringmatching(input,"hari")):
            #       jumlahHari = cariBerapaMingguAtauHari(input)
            #       deadlineFromNow(jumlahHari)
'''

# Berdasarkan jenis task
# cari tanggal/waktu (contoh: 3 minggu, 3 hari)
 # artinya kata penting lagi minggu sama hari
# yuuk dihitung minggu itu berapa, hari itu berapa:)

# Menampilkan deadline suatu task
def tanyakanDeadline(tugas):
    print(tanggalDeadline(tugas)) # tanggal Deadline sesuai penyimpanan

# Memperbaharui task tertentu
def perbaharuiTask(tugas):
    tugasAda=False
    for i in listOfDeadlines:
        if(listOfDeadlines[0]==tugas):
            tugasAda = True
            listOfDeadlines[1]=tanggalBaru
            break
    if(tugasGakAda()):
        print("Gak ada tuh di daftar task")

# Menandai sudah
def deleteTask(tugas):
    for i in listOfDeadlines:
        if(listOfDeadlines[0]==tugas)
            listOfDeadlines.remove(i) # ? wkwk tergantung datanya
        break

# Menampilkan opsi help
def help():
    print("Fitur") #dst
    print("Daftar kata penting")