def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    new_intervals = []
    for i, interval in enumerate(intervals):
        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]
        start = interval[0]
        end = interval[1]
        if new_interval_end < start:
            return new_intervals + [newInterval] + intervals[i:]
        elif new_interval_start > end:
            new_intervals.append(interval)
        else:
            newInterval = [min(start, new_interval_start), max(end, new_interval_end)]
        # if i == len(intervals):
        #     return new_intervals + [newInterval]
    return new_intervals + [newInterval]

# print(insert([[1, 3], [6, 9]]       , [2, 5]))

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],
                      [4,8]))