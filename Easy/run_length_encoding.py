"""Given a non-empty string, we are asked to write a function that is going to run
-length-encode the input string and return the encoded string. Run-length encoding 
refers to replacing repetitive, consecutive data by a count and one copy of a repeated 
data. For instance, AAABB will be encoded as 3A2B. If a sequence contains more than 9 
consecutive, identical characters, we first encode 9 characters, then the remaining ones. 
For instance, AAAAAAAAAA (10 As) will be encode as 9A1A
"""
#O(n) time | O(n) space -where n is the length of string
def runLengthEncoding(string):
    encodedStringCharacters=[]
    currentRunLength=1
    for i in range(1,len(string)):
        currentCharacter=string[i]
        previousCharacter=string[i-1]
        if currentCharacter!=previousCharacter or currentRunLength==9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)
            currentRunLength=0

        currentRunLength+=1
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string)-1])
    return ''.join(encodedStringCharacters)