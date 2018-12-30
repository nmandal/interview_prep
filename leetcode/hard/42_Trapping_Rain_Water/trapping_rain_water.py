# O(n) time | O(1) space
class Solution:
    def trap(self, height):
        i, j = 0, len(height) - 1
        left, right, water = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] > left:
                    left = height[i]
                else:
                    water += left - height[i]
                i += 1
            else:
                if height[j] > right:
                    right = height[j]
                else:
                    water += right - height[j]
                j -= 1
        return water
