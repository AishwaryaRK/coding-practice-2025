from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
