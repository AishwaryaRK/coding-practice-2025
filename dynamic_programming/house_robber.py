from typing import List


def rob(nums: List[int]) -> int:
    memoization = {}
    def dp(nums: List[int], i) -> List[int]:
        if not nums:
            return [0]
        if i in memoization:
            return memoization[i]
        result = []
        sub_results = dp(nums[2:], i + 2)
        if sub_results:
            for r in sub_results:
                result.append(nums[0] + r)
        else:
            result.append(nums[0])
        result += dp(nums[1:], i + 1)
        memoization[i] = result
        return result

    return max(dp(nums, 0))


# print(rob([2, 7, 9, 3, 1]))
# print(rob([1, 2, 3, 1]))
print(
    rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
         185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]))
