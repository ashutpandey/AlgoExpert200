#returns max sum subarray in the given array
def kadanesAlgorithm(array):
    maxEndingHere=array[0]
    maxSoFar=array[0]

    for i in range(1,len(array)):
        maxEndingHere=max(array[i],array[i]+maxEndingHere)
        maxSoFar=max(maxEndingHere,maxSoFar)
    return maxSoFar