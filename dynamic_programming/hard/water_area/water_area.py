# O(n) time | O(n) space - where n is the length of the input array
def water_area(heights):
    maxes = [0 for x in heights]
    left_max = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(left_max, height)
    right_max = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(right_max, maxes[i])
        if height < min_height:
            maxes[i] = min_height - height
        else:
            maxes[i] = 0
        right_max = max(right_max, height)
    return sum(maxes)
