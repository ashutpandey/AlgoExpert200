"""
write a function to find the longest peak in an array 
where a peak is a position in array from this peak to left and right 
side the elements are in strictly decreasing order (please note
that a peak must contain at least 3 elements and hence the start 
or the end indices can not be peaks)
return the longest peak in the array

input
[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
output 
10
explanation-

there are two peak 4 and 10 
of size 3 and 6 respectively as 10 has peak size 6
so 10 is returned
"""

def longestPeak(array):
    longestPeakLength=0
    i=1
    while i<len(array)-1:
        isPeak=array[i-1] <array[i] and array[i] > array[i+1]
        if not isPeak:
            i+=1
            continue
        leftIdx=i-2
        while leftIdx>=0 and array[leftIdx]<array[leftIdx+1]:
            leftIdx-=1
        rightIdx=i+2
        while rightIdx<len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx+=1
        currentPeakLength=rightIdx-leftIdx-1
        longestPeakLength=max(longestPeakLength,currentPeakLength)
        i=rightIdx
    return longestPeakLength







