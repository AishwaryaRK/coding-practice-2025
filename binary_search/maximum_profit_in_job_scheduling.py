from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    intervals = sorted(zip(startTime, endTime, profit))

    def nextInterval(i):
        start = i + 1
        end = len(intervals) - 1
        while start < end:
            mid = start + (end - start) // 2
            if intervals[mid][0] >= intervals[i][1]:
                end = mid
            else:
                start = mid + 1
        return start if start in range(len(intervals)) and intervals[start][0] >= intervals[i][1] else len(intervals)

    memoization = {}

    def backtracking(i):
        if i not in range(len(intervals)):
            return 0
        if i in memoization:
            return memoization[i]
        # for j in range(i,len(intervals)):
        interval = intervals[i]
        p1 = interval[2] + backtracking(nextInterval(i))
        p2 = backtracking(i + 1)
        p = max(p1, p2)
        memoization[i] = p
        return p

    return backtracking(0)


print(jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
