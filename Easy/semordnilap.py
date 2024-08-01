def semordnilap(words):
    wordSet=set(words)
    countPairs=[]
    for word in words:
        reverse=word[::-1]
        if reverse in wordSet and reverse!=word:
            countPairs.append([word,reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)
    return countPairs
