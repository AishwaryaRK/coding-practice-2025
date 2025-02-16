import collections
import heapq
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    freq = collections.defaultdict(int)
    for word in words:
        freq[word] += 1

    max_heap = []
    for word, freq in freq.items():
        heapq.heappush(max_heap, (-freq, word))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(max_heap)[1])
    return result


print(topKFrequent(["i", "lave", "leetcode", "leetcode","i", "lave", "coding"], k=3))
