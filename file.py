def readFile(fileName):
        fileObj = open(fileName, "r") 
        words = fileObj.read().splitlines() 
        fileObj.close()
        return words

print(readFile("katapenting.txt"))

data_deadline = ("27/04/2020 IF2210 Tubes String Matching\n")
with open('tugas.txt', 'a+') as f:
    f.write(data_deadline)
    
