# def diceThrows(numDice,numSides,target):
#     storedResults=[[-1]*(target+1) for _ in range(numDice+1)]
#     return diceThrowsHelper(numDice,numSides,target,storedResults)
# def diceThrowsHelper(numDice,numSides,target,storedResults):
#     if numDice==0:
#         return 1 if target==0 else 0
#     if storedResults[numDice][target]>-1:
#         return storedResults[numDice][target]
#     numWaysToReachTarget=0
#     for currentTarget in range(max(0,target-numSides),target):
#         numWaysToReachTarget+=diceThrowsHelper(numDice-1,numSides,currentTarget,storedResults)
#     storedResults[numDice][target]=numWaysToReachTarget
#     return numWaysToReachTarget

#O(d*s*t) | O(d*t) space
# def diceThrows(numDice,numSides,target):
#     storedResults=[[0]*(target+1) for _ in range(numDice+1)]
#     storedResults[0][0]=1
#     for currentNumDice in range(1,numDice+1):
#         for currentTarget in range(target+1):
#             numWaysToReachTarget=0
#             for currentNumSides in range(1,min(currentTarget,numSides)+1):
#                 numWaysToReachTarget+=storedResults[currentNumDice-1][currentTarget-currentNumSides]
#             storedResults[currentNumDice][currentTarget]=numWaysToReachTarget
#     return storedResults[numDice][target]

#O(d*s*t) time | O(t) space

def diceThrows(numDice,numSides,target):
    storedResults=[[0]*(target+1),[0]*(target+1)]
    storedResults[0][0]=1
    previousNumDiceIndex=0
    newNumDiceIndex=1
    for _ in range(numDice):
        for currentTarget in range(target+1):
            numWaysToReachTarget=0
            for currentNumSides in range(1,min(currentTarget,numSides)+1):
                numWaysToReachTarget+=storedResults[previousNumDiceIndex][currentTarget-currentNumSides]
            storedResults[newNumDiceIndex][currentTarget]=numWaysToReachTarget
        previousNumDiceIndex,newNumDiceIndex=newNumDiceIndex,previousNumDiceIndex
    return storedResults[previousNumDiceIndex][target]