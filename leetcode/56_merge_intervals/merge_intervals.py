# O(n log n) time | O(n) space

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        merged = []
        for ele in sorted(intervals, key=lambda x: x.start):
            if merged and ele.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, ele.end)
            else:
                merged.append(ele)
        return merged
