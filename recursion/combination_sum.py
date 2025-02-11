from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def decision_tree(candidates, target):
        if not candidates:
            return []

        # if len(candidates) == 1:
        #     if target == candidates[0]:
        #         return [candidates]
        #     return []

        n = candidates[0]
        if n > target:
            return decision_tree(candidates[1:], target)

        if target - n == 0:
            return [[n]]

        result = []
        combinations1 = decision_tree(candidates, target - n)
        combinations2 = decision_tree(candidates[1:], target)
        for c in combinations1:
            if c:
                result.append([n] + c)
        for c in combinations2:
            if c:
                result.append(c)
        return result

    return decision_tree(candidates, target)


print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
print(combinationSum([3, 5, 8], 11))
print(combinationSum([8,7,4,3], 11))
print(combinationSum([2,4,8], 8))