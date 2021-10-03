class Solution(object):
    trust_map={}
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)==0:
            return 1
        self.trust_map.clear()
        for i in range(1,N+1):
            self.trust_map[i]=[]
        #print self.trust_map
        for i,j in trust:
                self.trust_map[i].append(j)
                self.trust_map[j].append(0)

        judge=-1
        count=0
        isZero=1
        #print self.trust_map
        for k,v in self.trust_map.items():
            for i in v:
                if i!=0:
                    isZero=0
            if isZero==1:
                judge=k
                count=count+1
            isZero=1
        if isZero==1 and count>1:
            return -1

        #allTrust=0
        for k,v in self.trust_map.items():
            if judge==k:
                continue
            if judge not in v:
                judge=-1
        #print self.trust_map
        return judge
                
