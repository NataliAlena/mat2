file = open ("text.txt" ,"r")
Word = file.readline().rstrip()
read = file.read().split()
file.close()
def revWord (string):
    wordreverse = string[::-1]
    return wordreverse.lower()
def countWord(file,Word):
    cword = 1
    for line in read:
        words = line.split()
        for word in words:
            revword= revWord(word)
            if Word==revword:
                cword+=1
    return cword

