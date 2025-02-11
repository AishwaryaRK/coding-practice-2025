from typing import List


def trap(height: List[int]) -> int:
    max_l = 0
    max_r = 0
    l = 0
    r = len(height) - 1
    water = 0
    while l <= r:
        if max_l < max_r:
            water_l = max_l - height[l]
            if water_l > 0:
                water += water_l
            max_l = max(max_l, height[l])
            l += 1
        else:
            water_r = max_r - height[r]
            if water_r > 0:
                water += water_r
            max_r = max(max_r, height[r])
            r -= 1
    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
