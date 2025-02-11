from typing import List


# [1, 2, 3]
# []
# [], [1]
# [], [1], [2], [1,2]
# [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        temp_result = []
        for r in result:
            temp_result.append(r + [num])
        result += temp_result
    return result


print(subsets([1, 2, 3]))
