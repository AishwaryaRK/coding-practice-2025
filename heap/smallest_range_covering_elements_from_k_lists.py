import heapq
import math
from typing import List


def smallestRange(nums: List[List[int]]) -> List[int]:
    smallest_range = [0, 0]
    smallest_range_diff = math.inf
    min_heap = []
    max_heap = []
    for i, num in enumerate(nums):
        heapq.heappush(min_heap, (num[0], i, 0))
        heapq.heappush(max_heap, (-num[0], i, 0))
    while True:
        min_num, i, ele_i = heapq.heappop(min_heap)
        max_num, _, _ = max_heap[0]
        max_num = -max_num
        if max_num - min_num < smallest_range_diff:
            smallest_range = [min_num, max_num]
            smallest_range_diff = max_num - min_num
        if ele_i + 1 >= len(nums[i]):
            break
        heapq.heappush(min_heap, (nums[i][ele_i + 1], i, ele_i + 1))
        heapq.heappush(max_heap, (-nums[i][ele_i + 1], i, ele_i + 1))

    return smallest_range


print(smallestRange(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]]))