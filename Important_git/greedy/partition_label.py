class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        last={}


        for i,s in enumerate(S):
                last[s]=i

        ans=[]
        start=0
        end=0
        for i,s in enumerate(S):
            #get max last occurance in the window
            end=max(end,last[s])
            #if i== last most occurance then append ans
            if i==end:
                ans.append(end-start+1)
                start=i+1

        #print ans
        return ans
