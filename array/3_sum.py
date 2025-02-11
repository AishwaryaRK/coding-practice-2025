nums_map = {}
def threeSum(nums):
    results = []
    for n in nums:
        result = twoSum(nums, -n, n)
        if len(result) != 0:
            results.append([n] + result)
    return results


def twoSum(nums, target, num):
    for i, n in enumerate(nums):
        if n != num and (target - n) in nums_map:
            return [n, target - n]
        nums_map[n] = i
    return []

print(threeSum([-1,0,1,2,-1,-4]))