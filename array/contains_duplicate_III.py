from typing import List
# import bisect
def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    if indexDiff == 0 or indexDiff >= len(nums):
        return False
    # bisect.bisect_left()
    for i in range(len(nums) - indexDiff):
        for j in range(i + 1, i + indexDiff + 1):
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False


print(containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], indexDiff=3, valueDiff=0))
print(containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], indexDiff=2, valueDiff=3))
print(containsNearbyAlmostDuplicate(nums=[-2, 3], indexDiff=2, valueDiff=5))
