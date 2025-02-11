from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    result = []
    for i, num in enumerate(nums):
        permutations = permute(nums[:i] + nums[i + 1:])
        for permutation in permutations:
            result.append([num] + permutation)
    return result


print(permute([1, 2, 3]))
