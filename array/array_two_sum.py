def twoSum(nums, target):
    nums_map = {}
    for i,n in enumerate(nums):
        if (target-n) in nums_map:
            return [i,nums_map[target-n]]
        nums_map[n]=i
    return []


