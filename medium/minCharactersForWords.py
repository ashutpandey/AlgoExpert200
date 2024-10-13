#O(n*l) time | O(c) space
def minimumCharacterForWords(words):
    maximumCharacterFrequencies={}
    for word in words:
        characterFrequencies=countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies,maximumCharacterFrequencies)
    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)
def countCharacterFrequencies(string):
    characterFrequencies={}
    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character]=0
        characterFrequencies[character]+=1
    return characterFrequencies

def updateMaximumFrequencies(frequencies,maximumFrequencies):
    for character in frequencies:
        frequency=frequencies[character]
        if character in maximumFrequencies:
            maximumFrequencies[character]=max(frequency,maximumFrequencies[character])
        else:
            maximumFrequencies[character]=frequency


def makeArrayFromCharacterFrequencies(maximumCharacterFrequencies):
    ans=[]
    for character in maximumCharacterFrequencies:
        for _ in range(maximumCharacterFrequencies[character]):
            ans.append(character)
    return ans