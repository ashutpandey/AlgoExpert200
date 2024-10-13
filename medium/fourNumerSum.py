def fourNumberSum(array,targetSum):
    allPairSums={}
    quadruplets=[]
    for i in range(1,len(array)-1):
        for j in range(i+1,len(array)):
            currentSum=array[i]+array[j]
            differnece=targetSum-currentSum
            if differnece in allPairSums:
                for pair in allPairSums[differnece]:
                    quadruplets.append(pair+[array[i],array[j]])
        for k in range(0,i):
            currentSum=array[i]+array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum]=[[array[k],array[i]]]
            else:
                allPairSums[currentSum].append([array[k],array[i]])

