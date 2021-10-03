class Solution(object):

    def helper(self,cand,cand_list,sum1,target,seen,out):

        if sum1>target:
            return

        if sum1==target:
            #print "target"
            t=tuple(sorted(cand_list))
            if t in seen:
                return
            seen[t]=1
            out.append(cand_list[:]) # give it a copy since list is pass by reference
            return

        #print cand_list
        for i in range(len(cand)):

            chosen=cand[i]
            sum1_tmp=sum1 #get from parent for each iteration
            sum1_tmp+=chosen
            cand_list.append(chosen)

            self.helper(cand,cand_list,sum1_tmp,target,seen,out)
            cand_list.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        c=[]
        seen={}
        out=[]
        self.helper(candidates,c,0,target,seen,out)
        #print out.sort(key=lambda x:x[0])
        return out
