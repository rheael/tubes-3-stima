import * from RegularExpression
import * from kmpstringmatching

''' BARU GAMBARAN '''
# Harus diintegrasikan sama penyimpanan data

def pilihanInput(input): # Masuk ke fitur sesuai masukan pengguna
    if(kmpstringmatching(input,"kapan")):
        tanyakanDeadline(re.match(re.compile("IF+[0-9]")))
    elif(kmpstringmatching(input,"diundur")):
        perbaharuiTask(re.match(re.compile("IF+[0-9]")))
    elif(kmpstringmatching(input,"selesai")):
        deleteTask(re.match(re.compile("IF+[0-9]")))
    elif(kmpstringmatching(input,"help")):
        help()
    elif(kmpstringmatching(input,"tampilkan")):
        tampilkanSeluruhDeadline()
    else:
        print("Maaf, pesan tidak dikenali\n")

'''
# Menambahkan task baru
def addTask(tanggal,kode,jenis,topik):
    input = input("Masukkan task: " )
    print("[TASK BERHASIL DICATAT]\n")
    print((ID:1) 14/04/2021 - IF2211 - Tubes - String matching)
    ID = len(listOfDeadlines)+1
    tanggal = readDate(input)
    kodematkul = re.match("IF",....)
    jenis = re.match() # semua kata penting
    #topik = semua setelah semua kata penting yang bukan tanggal, bukan stopwords
'''

def tampilkanSeluruhDeadline():
    for i in listOfDeadlines:
        print(i)

'''
# Melihat daftar task yang harus dikerjakan
# Seluruh task

# Berdasarkan periode waktu, udah ada di RegularExpression.py

# Berdasarkan jenis task
if(kataPenting(input)==true):
    # cari tanggal/waktu (contoh: 3 minggu, 3 hari)
    # artinya kata penting lagi minggu sama hari
    # yuuk dihitung minggu itu berapa, hari itu berapa:)
'''

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
    deleteTugas(tugas)

# Menampilkan opsi help
def help():
    if(input==help()): # misal ngomong asisten bisa apa
        print("Fitur") #dst
        print("Daftar kata penting")