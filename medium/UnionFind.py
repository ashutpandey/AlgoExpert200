# class UnionFind:
#     def __init__(self):
#         self.parents={}
#     #O(1) time | O(1) space
#     def createSet(self,value):
#         self.parents[value]=value
#     #O(n) time | O(1) space
#     def find(self,value):
#         if value not in self.parents:
#             return None
#         currentParent=value
#         while currentParent!=self.parents[currentParent]:
#             currentParent=self.parents[currentParent]
#         return currentParent
    
#     #O(n) time | O(1) space
#     def union(self,valueOne,valueTwo):
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return
#         valueOneRoot=self.find(valueOne)
#         valueTwoRoot=self.find(valueTwo)

#         self.parents[valueTwoRoot]=valueOneRoot



# class UnionFind:
#     def __init__(self):
#         self.parents={}
#         self.ranks={}
#     #O(1) time | O(1) space
#     def createSet(self,value):
#         self.parents[value]=value
#         self.ranks[value]=0
#     #O(log(n)) time | O(1) space
#     def find(self,value):
#         if value not in self.parents:
#             return None
#         currentParent=value
#         while currentParent!=self.parents[currentParent]:
#             currentParent=self.parents[currentParent]
#         return currentParent
    
#     #O(log(n)) time | O(1) space
#     def union(self,valueOne,valueTwo):
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return
#         valueOneRoot=self.find(valueOne)
#         valueTwoRoot=self.find(valueTwo)

#         if self.ranks[valueOneRoot]<self.ranks[valueTwoRoot]:
#             self.parents[valueOneRoot]=valueTwoRoot
#         elif self.ranks[valueOneRoot]>self.ranks[valueTwoRoot]:
#             self.parents[valueTwoRoot]=valueOneRoot
#         else:
#             self.parents[valueTwoRoot]=valueOneRoot
#             self.ranks[valueOneRoot]+=1


class UnionFind:
    def __init__(self):
        self.parents={}
        self.ranks={}
    #O(1) time | O(1) space
    def createSet(self,value):
        self.parents[value]=value
        self.ranks[value]=0
    #O(α(n)),approx O(1) time |O(α(n)),approx O(1) space
    def find(self,value):
        if value not in self.parents:
            return None
        if value!=self.parents[value]:
            self.parents[value]=self.find(self.parents[value])
        return self.parents[value]
    
    #O(α(n)),approx O(1) time |O(α(n)),approx O(1) space
    def union(self,valueOne,valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot=self.find(valueOne)
        valueTwoRoot=self.find(valueTwo)

        if self.ranks[valueOneRoot]<self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot]=valueTwoRoot
        elif self.ranks[valueOneRoot]>self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot]=valueOneRoot
        else:
            self.parents[valueTwoRoot]=valueOneRoot
            self.ranks[valueOneRoot]+=1


