#https://leetcode.com/problems/insert-interval/submissions/
class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals)==0:
            return [newInterval]

        s,e=newInterval
        #intervals.sort()
        inserted=False
        #insert
        for i,interval in enumerate(intervals):
            s1,e1=interval
            if s1<=s<=e1:
                inserted=True
                intervals[i][1]=max(e,e1)
                break
        if not inserted:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])

        #check for merges
        out=[intervals[0]]
        start=0
        for i,interval in enumerate(intervals[1:]):
            s1,e1 = interval
            s,e = out[start]
            if s<=s1<=e:
                out[start][1]=max(e,e1)
            else:
                out.append(interval)
                start+=1
        return out
            
