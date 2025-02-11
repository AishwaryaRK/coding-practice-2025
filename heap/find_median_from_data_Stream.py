import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_heap_len = 0
        self.min_heap_len = 0

    def addNum(self, num: int) -> None:
        if self.max_heap_len == 0:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_len += 1
            return
        left_num = -self.max_heap[0]
        if num <= left_num:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_len += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_len += 1
        if abs(self.max_heap_len - self.min_heap_len) > 1:
            if self.max_heap_len > self.min_heap_len:
                n = -heapq.heappop(self.max_heap)
                self.max_heap_len -= 1
                heapq.heappush(self.min_heap, n)
                self.min_heap_len += 1
            else:
                n = heapq.heappop(self.min_heap)
                self.min_heap_len -= 1
                heapq.heappush(self.max_heap, -n)
                self.max_heap_len += 1

    def findMedian(self) -> float:
        # print("------")
        # print(self.max_heap)
        # print(self.min_heap)
        if (self.max_heap_len + self.min_heap_len) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return -self.max_heap[0] if self.max_heap_len > self.min_heap_len else self.min_heap[0]


# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())


# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
