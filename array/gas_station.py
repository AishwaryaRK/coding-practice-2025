from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    diff = [g - c for g, c in zip(gas, cost)]
    if sum(diff) < 0:
        return -1
    index = -1
    total = 0
    for i, d in enumerate(diff):
        if total + d < 0:
            total = 0
            index = -1
        else:
            total += d
            if index == -1:
                index = i
    return index


print(canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(canCompleteCircuit(gas=[1, 5, 3, 2, 4], cost=[3, 2, 5, 4, 1]))
print(canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
