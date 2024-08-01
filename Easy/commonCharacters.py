# def commonCharacters(strings):
#     smallestString=strings[0]
#     for i in range(1,len(strings)):
#         if len(strings[i])<len(smallestString):
#             smallestString=strings[i]
#     st=set(smallestString)
#     for i in range(len(strings)):
#         st1=set(strings[i])
#         aux=[]
#         for ele in st:
#             if ele not in st1:
#                 aux.append(ele)
#         for t in aux:
#             st.remove(t)
#     return list(st)


# arr=['abc','bcd','abccad']
# def main():
#     ans=commonCharacters(arr)
#     print(ans)



# def commonCharacters(strings):
#     characterCounts={}
#     for string in strings:
#         uniqueStringCharacters=set(string)
#         for character in uniqueStringCharacters:
#             if character not in characterCounts:
#                 characterCounts[character]=0
#             characterCounts[character]+=1
#     finalCharacters=[]
#     for character, count in characterCounts.items():
#         if count==len(strings):
#             finalCharacters.append(character)
#     return finalCharacters



def commonCharacters(strings):
    smallestString=getSmallestString(strings)
    potentialCommonCharacters=set(smallestString)

    for string in strings:
        removeNonexistantCharacters(string,potentialCommonCharacters)
    return list(potentialCommonCharacters)
def getSmallestString(strings):
    smallestString=strings[0]
    for string in strings:
        if len(string)<len(smallestString):
            smallestString=string
    return smallestString


def removeNonexistantCharacters(string,potentialCommonCharacters):
    uniqueStringCharacters=set(string)
    for character in list(potentialCommonCharacters):
        if character not in uniqueStringCharacters:
            potentialCommonCharacters.remove(character)



def main():
    arr=['abc','bcd','baccad']
    ans=commonCharacters(arr)
    print(ans)

if __name__=="__main__":
    main()




