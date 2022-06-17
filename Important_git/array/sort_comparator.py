#https://leetcode.com/problems/reorder-data-in-log-files/solution/
class Solution:
    def get_key(self,log):
        l = log.split(" ")
        id, rest = l[0],l[1:]
        #print _id,rest
        if rest[0].isalpha():
            #key is in sorted order, first key0,if key0 is same then key1 is looked etc
            return (0, rest, id)
        else:
             return (1, )

    def reorderLogFiles(self, logs):
        #for each log in logs , key is called
        return sorted(logs, key=self.get_key)

def x(tup):
    #print tup
    #return (tup[1])
    return (tup[1])

a=[('c',-1),('b',8),('d',2),('a',2)]
a.sort(key=x)
print a

s=Solution()
logs=["j je", "b fjt", "7 zbr", "m le", "o 33"]
print s.reorderLogFiles(logs)
