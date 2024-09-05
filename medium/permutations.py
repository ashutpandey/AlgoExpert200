#Upper Bound O(n^2*n!) |O(n*n!)

# def getPermutations(array):
#     permutaitions=[]
#     permutationHelper(array,[],permutaitions)
# def permutationHelper(array,currentPermuation,permutations):
#     if not len(array) and len(currentPermuation):
#         permutations.append(currentPermuation)
#     else:
#         for i in range(array):
#             newArray=array[:i]+array[i+1:]
#             newPermutaiton=currentPermuation+[array[i]]
#             permutationHelper(newArray,newPermutaiton,permutations)


#O(n*n!) time | O(n*n!) space


#this is because we're not doing any O(n) operation in the loops


# 2*(n*n!) +O(n*n!)
def getPermutations(array):
    permutations=[]
    permutationsHelper(0,array,permutations)
def permutationsHelper(i,array,permutations):
    if i==len(array)-1:
        permutations.append(array[:])
    else:
        for j in range(i,len(array)):
            swap(array,i,j)
            permutationsHelper(i+1,array,permutations)
            swap(array,i,j)

def swap(array,i,j):
    array[i],array[j]=array[j],array[i]




