#O(n^3) time| O(n^2) space
# def juiceBottling(prices):
#     numSizes=len(prices)
#     maxProfit=[0]*numSizes
#     solutions=[[]]*numSizes
#     for size in prices:
#         for dividingPoint in range(size+1):
#             possibleProfit=maxProfit[size-dividingPoint]+prices[dividingPoint]
#             if possibleProfit>maxProfit[size]:
#                 maxProfit[size]=possibleProfit
#                 solutions[size]=[dividingPoint]+solutions[size-dividingPoint]
#     return solutions[numSizes-1]

#O(n^2) time | O(n) space
def juiceBottling(prices):
    numSizes=len(prices)
    maxProfit=[0]*numSizes
    solutions=[0]*numSizes
    for size in prices:
        for dividingPoint in range(size+1):
            possibleProfit=maxProfit[size-dividingPoint]+prices[dividingPoint]
            if possibleProfit>maxProfit[size]:
                maxProfit[size]=possibleProfit
                dividingPoint[size]=dividingPoint
    solutions=[]
    currentDividingPoint=numSizes-1
    while currentDividingPoint>0:
        solutions.append(dividingPoint[currentDividingPoint])
        currentDividingPoint-=dividingPoint[currentDividingPoint]
    return solutions


