# O(n) time | O(1) space
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(nums) == len(set(nums))
