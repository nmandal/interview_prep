# O(N) time | O(1) space
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        i = 0
        for ch in s:
            if count[ch] == 1:
                return i
            else:
                i += 1
        return -1
