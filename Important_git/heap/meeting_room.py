class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if len(intervals)==0:
            return 0

        rooms=[]
        intervals.sort(key= lambda x:x[0])
        #print intervals
        #push end times to the min-heap
        heapq.heappush(rooms,intervals[0][1])

        for meeting in intervals[1:]:
            s,e=meeting[0],meeting[1]
            if s>=rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms,e)

        return len(rooms)
