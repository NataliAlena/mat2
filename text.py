file = open ("text.txt" ,"r")
originalWord = file.readline().rstrip()
read = file.read().split()
file.close()
def revword (string):
    word = string[::-1]
    return word.lower()

def countword( ):
    cword = 1
    for line in read:
        words = line.split()
        for word in words:
            rev= revword(word)
            if originalWord==rev:
                cword+=1
    return cword

