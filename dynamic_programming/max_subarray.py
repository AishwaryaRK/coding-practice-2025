from typing import List


# sliding window
def maxSubArray(nums: List[int]) -> int:
    s = nums[0]
    total = 0
    for n in nums:
        if total + n > 0:
            total += n
        else:
            total = 0
        s = max(s, total)
    return s


# print(maxSubArray([2, 4, -8, 4]))
# # print(maxSubArray([2, 3, -3, 4]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
