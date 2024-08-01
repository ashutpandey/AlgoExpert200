# def generateDocument(characters,document):
#     for character in document:
#         documentFrequency=countCharacterFrequency(character,document)
#         characterFrequency=countCharacterFrequency(character,characters)
#         if documentFrequency>characterFrequency:
#             return False
        
#         return True
# def countCharacterFrequency(character,target):
#     frequency=0
#     for char in target:
#         if char==character:
#             frequency+=1
#     return frequency



# def generateDocument(characters,document):
#     alreadyCounted=set()
#     for character in document:
#         if character in alreadyCounted:
#             continue
#         documentFrequency=countCharacterFrequency(character,document)
#         characterFrequency=countCharacterFrequency(character,characters)
#         if documentFrequency>characterFrequency:
#             return False
        
#         alreadyCounted.add(character)
#         return True
# def countCharacterFrequency(character,target):
#     frequency=0
#     for char in target:
#         if char==character:
#             frequency+=1
#     return frequency

#O(n+m) time | O(c) space
def generateDocument(characters,document):
    characterCount={}
    for character in characters:
        if character not in characterCount:
            characterCount[character]=0
        characterCount[character]+=1
    for character in document:
        if character not in characterCount or characterCount[character]==0:
            return False
        characterCount[character]-=1
    return True


