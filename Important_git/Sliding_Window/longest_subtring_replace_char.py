class Solution(object):

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s)<=k:
            return len(s)

        letter_count=[0 for i in range(26)]

        """
        constraint for valid window =  (window size)-(max char count) <=k

        """
        
        st=0
        ed=0
        maxChar=float('-inf')
        max_ans=float('-inf')
        while ed<len(s):
            #print st,ed,
            letter_count[ord(s[ed])-ord('A')]+=1

            window_size=ed-st+1
            maxChar=max(letter_count)
            replace_count = window_size-maxChar

            if replace_count<=k:
                #valid window
                max_ans=max(max_ans,window_size)
            else:
                letter_count[ord(s[st])-ord('A')]-=1
                st+=1
            ed+=1
            #print letter_count
        return max_ans
