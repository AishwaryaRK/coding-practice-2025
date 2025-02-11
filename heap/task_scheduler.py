import collections
import heapq
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    cpu_intervals = 0

    task_count = collections.defaultdict(int)
    for task in tasks:
        task_count[task] += 1

    h = []
    for task, count in task_count.items():
        heapq.heappush(h, [-count, task])

    tasks_scheduled = 0
    waiting_tasks_queue = collections.deque()
    while tasks_scheduled != len(tasks):
        if len(h) == 0:
            cpu_intervals += 1  # add idle
        else:
            count, task = heapq.heappop(h)
            tasks_scheduled += 1
            cpu_intervals += 1
            count -= (-1)
            if count != 0:
                waiting_tasks_queue.append([count, task, cpu_intervals])
        if waiting_tasks_queue and waiting_tasks_queue[0][2] + n <= cpu_intervals:
            count, task, _ = waiting_tasks_queue.popleft()
            heapq.heappush(h, [count, task])

    return cpu_intervals


print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))
