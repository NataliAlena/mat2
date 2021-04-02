def revword (string):
    wordreverse = string[::-1]
    return wordreverse.lower()
def countword(read):
    file = open ('text.txt',"r")
    Word = file.readline().rstrip()
    read = file.read().split()
    file.close()
    cword = 1
    for line in read:
        words = line.split()
        for word in words:
            revw= revword(word)
            if Word==revw:
                cword+=1
    return cword
