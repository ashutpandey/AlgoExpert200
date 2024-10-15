def knapsackProblem(items,capacity):
    knapsackValues=[[0 for x in range(0,capacity+1)]for y in range(0,len(items)+1)]
    for i in range(1,len(items)+1):
        currentWeight=items[i-1][1]
        currentValue=items[i-1][0]
        for c in range(0,capacity+1):
            if currentWeight>c:
                knapsackValues[i][c]=knapsackValues[i-1][c]
            else:
                knapsackValues[i][c]=max(knapsackValues[i-1][c],knapsackValues[i-1][c-currentWeight]+currentValue)
    return [knapsackValues[-1][-1],getKnapSackItems(knapsackValues,items)]
def getKnapSackItems(knapSackValues,items):
    sequence=[]
    i=len(knapSackValues)-1
    c=len(knapSackValues[0])-1
    while i>0:
        if knapSackValues[i][c]==knapSackValues[i-1][c]:
            i-=1
        else:
            sequence.append(i-1)
            c-=items[i-1][1]
            i-=1
        if c==0:
            break
    return list(reversed(sequence))



