from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    positive_nums = [0] * (n)
    for num in nums:
        if num in range(1, n+1):
            positive_nums[num - 1] = 1
    for i, num in enumerate(positive_nums):
        if num == 0:
            return i + 1
    return n + 1


# print(firstMissingPositive([1, 2, 0]))
# print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([1]))
