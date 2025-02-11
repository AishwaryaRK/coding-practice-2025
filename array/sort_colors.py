from typing import List


def sortColors(nums: List[int]) -> None:
    red = 0
    blue = len(nums) - 1
    i = 0
    while i <= blue and red in range(len(nums)) and blue in range(len(nums)):
        while red in range(len(nums)) and nums[red] == 0:
            red += 1
        while blue in range(len(nums)) and nums[blue] == 2:
            blue -= 1
        # while nums[red] == 2 and nums[blue] == 0:
        #     nums[red] = 0
        #     red += 1
        #     nums[blue] = 2
        #     blue -= 1
        if red not in range(len(nums)) or blue not in range(len(nums)) or red >= blue:
            break
        if i < red:
            i = red
        if nums[i] == 2:
            t = nums[blue]
            nums[blue] = nums[i]
            blue -= 1
            nums[i] = t
        if nums[i] == 0:
            t = nums[red]
            nums[red] = nums[i]
            red += 1
            nums[i] = t
        i += 1
    print(nums)


# sortColors([2, 0, 2, 1, 1, 0])
# sortColors([2, 0, 1])
# sortColors([0])
# sortColors([0, 1, 0])
# sortColors([2, 1, 2])
sortColors([0, 2])
