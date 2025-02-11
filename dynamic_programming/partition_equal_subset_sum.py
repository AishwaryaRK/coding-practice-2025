from typing import List


# def canPartition(nums: List[int]) -> bool:
#     s = sum(nums)
#     if s % 2 != 0:
#         return False
#
#     target = s // 2
#
#     def dp(nums, left_sum, right_sum):
#         if left_sum == target or right_sum == target:
#             return True
#         if left_sum > target or right_sum > target:
#             return False
#         if not nums:
#             return left_sum == right_sum
#
#         return dp(nums[1:], left_sum + nums[0], right_sum) or dp(nums[1:], left_sum, right_sum + nums[0])
#
#     return dp(nums, 0, 0)


def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False  # If the sum is odd, it's impossible to split equally.

    target = total_sum // 2
    dp = set([0])  # Store all possible subset sums

    for num in nums:
        new_dp = dp.copy()
        for partial_sum in dp:
            if partial_sum + num == target:
                return True
            new_dp.add(partial_sum + num)
        dp = new_dp

    return target in dp


print(canPartition([1, 5, 5, 11]))
# print(canPartition([1, 2, 3, 5]))
# print(canPartition(
#     [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]
#     ))
