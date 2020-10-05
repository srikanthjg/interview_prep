class Solution(object):
    def isAnagram(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        return sorted(str1)==sorted(str2)

    def compare(self,group,val):
    #print val
        while(len(val)):
            row=[]
            if(len(val)==1):
                row.append(val[0])
                val.remove(val[0])
                group.append(row)
                break
            else:
                i=1
                while(i<len(val)):
                    if(self.isAnagram(val[0],val[i])):
                        row.append(val[i])
                        val.remove(val[i])
                    else:
                        i=i+1
                row.append(val[0])
                val.remove(val[0])
                group.append(row)
        return group

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #sort by length of string
        lenDict={}
        list=[]
        for str in strs:
            key=len(str)
            if(key not in lenDict):
                lenDict[key] = []
            lenDict[key].append(str)


        groupAnagrams=[]
        for key,val in lenDict.items():
             print self.compare(groupAnagrams,val)




    def groupAnagrams2(self,str):
        ## key is the sorted word which should be the same
        hmap={}
        #output=[]
        for s1 in str:

             string = "".join(sorted(s1))
             if(string not in hmap):
                 hmap[string] = []
                 hmap[string].append(s1)
             else:
                hmap[string].append(s1)

        return hmap.values()


input=["eat", "tea", "tan", "ate", "nat", "bat","list"]
sol = Solution()
#sol.groupAnagrams(input)
print sol.groupAnagrams2(input)



#print sol.isAnagram(input[1],input[0])
