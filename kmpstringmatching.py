#string matching dengan metode KMP 

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


#contohstring = "ham him hem"
#contohtext = "em"
#print(len(contohstring))
#print(contohstring[2])
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

contohstring = "ham him hem"
contohtext = "ham him"
ketemu = kmpstringmatching(contohstring,contohtext)

if(ketemu == False):
    print("X")
else:
    print("V")
