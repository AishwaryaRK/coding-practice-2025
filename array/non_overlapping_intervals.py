from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda e: e[1])
    c = 0
    prev_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_interval[1]:
            # if (prev_interval[1] - prev_interval[0]) > (intervals[i][1] - intervals[i][0]):
            #     prev_interval = intervals[i]
            c += 1
        else:
            prev_interval=intervals[i]
    return c


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(eraseOverlapIntervals([[1, 2], [2, 3]]))
print(eraseOverlapIntervals([ [1, 3], [2, 4],[0, 2], [3, 5], [4, 6]]))
