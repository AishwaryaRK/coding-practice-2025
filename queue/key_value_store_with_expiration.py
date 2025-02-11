"""
- [ ]  Concurrency Focused - Design a cache similar to LRU but focus was how to handle concurrent reads and writes,
locks, etc...
- [ ]  Least recently used Cache

    Given a window size, perform get, put, and average operation
    items that were added before the window size should be removed while taking average as well,
    and also during get operation, return null if item expired.

    window size 1hr

     Key-value store with expiration. Functions: put(key, value), get(key), and get_average()
     (average of non-expired values). Data streamed in order of increasing timestamps.

    00:00 put("A",10)

    00:10 put("B",20)

    00:30 average() -> 15

    01:05 average () -> 20

    01:08 get("B") -> 20

    01:15 put("A",30)

    01:50 average -> 30
"""
import collections
from datetime import datetime
from typing import Optional


class KeyValueStore:
    def __init__(self, window_size_sec=10):
        self.window_size_sec = window_size_sec
        self.store = collections.defaultdict(list)

    def __is_timestamp_in_window(self, t1: datetime, t2: datetime) -> bool:
        # if t2 < t1:
        #     t2 = t2.replace(day=t2.day + 1)
        diff = abs(t2 - t1)
        diff_sec = diff.total_seconds()
        if diff_sec <= self.window_size_sec:
            return True
        return False

    def put(self, time: str, key: str, value: int):
        timestamp = datetime.strptime(time, "%H:%M")
        self.store[key].append((timestamp, value))

    def get(self, time: str, key: str) -> Optional[int]:
        if key not in self.store:
            return None
        query_timestamp = datetime.strptime(time, "%H:%M")
        timestamp, val = self.store[key][-1]
        if self.__is_timestamp_in_window(timestamp, query_timestamp):
            return val
        else:
            return None

    def average(self, time: str) -> float:
        avg = 0
        n = 0
        query_timestamp = datetime.strptime(time, "%H:%M")
        for key, values in self.store.items():
            timestamp, val = values[-1]
            if self.__is_timestamp_in_window(timestamp, query_timestamp):
                n += 1
                avg += val
        return avg / n if n != 0 else 0


store = KeyValueStore(10 * 60)  # 10 mins
# store.put("01:00", "A", 20)
# store.put("01:03", "B", 10)
# store.put("01:05", "C", 30)
# print(store.average("01:14"))
# store.put("01:06", "A", 80)
# print(store.average("01:07"))
# print(store.get("01:14", "A"))
# print(store.average("01:15"))
# print(store.average("01:17"))

store.put("00:00", "A", 20)
store.put("01:03", "B", 10)
store.put("01:05", "C", 30)
print(store.average("01:10"))