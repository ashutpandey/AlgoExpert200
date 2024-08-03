#O(n^2) time | O(1) space
# def firstDuplicateValue(array):
#     minimumSecondIndex=len(array)
#     for i in range(len(array)):
#         value=array[i]
#         for j in range(i+1,len(array)):
#             valueToCompare=array[j]
#             if value==valueToCompare:
#                 minimumSecondIndex=min(minimumSecondIndex,j)
#     if minimumSecondIndex==len(array):
#         return -1
#     return array[minimumSecondIndex]

#O(n) time| O(n) space
# def firstDuplicate(array):
#     seen=set()
#     for value in array:
#         if value in seen:
#             return value
#         seen.add(value)
#     return -1

#O(n) time | O(1) space
def firstDuplicateValue(array):
    for value in array:
        absValue=abs(value)
        if array[absValue-1]<0:
            return absValue
        array[absValue-1]*=-1
    return -1



