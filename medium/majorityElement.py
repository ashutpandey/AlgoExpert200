#O(n) time | O(1) space
def majorityElement(array):
    answer=0
    for currentBit in range(32):
        currentBitValue=1<<currentBit
        onesCount=0
        for num in array:
            if (num& currentBitValue)!=0:
                onesCount+=1
            if onesCount>len(array)/2:
                answer+=currentBitValue
    return answer


#O(n) time | O(1) space
def majorityElement(array):
    answer=None
    count=0
    for num in array:
        if count==0:
            answer=num
        if num==answer:
            count+=1
        else:
            count-=1
    return answer