file = open ('text.txt',"r")
Word = file.readline().rstrip()
read = file.read().split()
file.close()
def revWord (string):
    wordreverse = string[::-1]
    return wordreverse.lower()
def countWord():
    cword=1
    i=0
    while i<len(read):
        read[i]=revWord(read[i])
        if read[i]==Word:
            cword=cword + 1
        i=i+1
        return cword