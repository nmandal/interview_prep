# O(n log n) time | O(n) space

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals) == 1:
            return len(intervals)
        heap = []
        min_num_rooms = 1
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start >= intervals[i-1].end:
                continue
            else:
                heapq.heappush(heap, intervals[i-1].end)
                if heap[0] <= intervals[i].start:
                    heapq.heappop(heap)
                else:
                    min_num_rooms += 1
        return min_num_rooms
