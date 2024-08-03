#O(n) time | O(n) space
# def missingNumbers(nums):
#     includedNums=set(nums)
#     solution=[]

#     for num in range(1,len(nums)+3):
#         if not num in includedNums:
#             solution.append(num)
#     return solution


#O(n) time| O(1) space
# def missingNumbers(nums):
#     total=sum(1,len(nums)+3)
#     for num in nums:
#         total-=num

#     averageMissingValue=total//2

#     foundFirstHalf=0
#     foundSecondHalf=0

#     for num in nums:
#         if num<=averageMissingValue:
#             foundFirstHalf+=num
#         else:
#             foundSecondHalf+=num

#     expectedFirstHalf=sum(range(1,averageMissingValue+1))
#     expectedSecondHalf=sum(range(averageMissingValue+1,len(nums)+3))
#     return [expectedFirstHalf-foundFirstHalf,expectedSecondHalf-foundSecondHalf]



def missingNumbers(nums):
    solutionXOR=0
    for i in range(0,len(nums)+3):
        solutionXOR^=i

        if i <len(nums):
            solutionXOR^=nums[i]
    solution=[0,0]

    setBit=solutionXOR&-solutionXOR
    for i in range(0,len(nums)+3):
        if i & setBit==0:
            solution[0]^=i
        else:
            solution[1]^=i
        if i <len(nums):
            if nums[i] & setBit==0:
                solution[0]^=nums[i]
            else:
                solution[1]^=nums[i]
    return sorted(solution)
