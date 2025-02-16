import heapq
from typing import List


# def min_meeting_rooms(meetings: List[List[int]]) -> int:
#     if not meetings:
#         return 0
#     meetings = sorted(meetings, key=lambda e: e[0])
#     min_meeting_rooms = 1
#     last_meeting_end = 0
#     for meeting in meetings:
#         if meeting[0] < last_meeting_end:
#             min_meeting_rooms += 1
#             last_meeting_end = max(last_meeting_end, meeting[1])
#         else:
#             last_meeting_end = meeting[1]
#     return min_meeting_rooms

def min_meeting_rooms(meetings: List[List[int]]) -> int:
    if not meetings:
        return 0
    meetings = sorted(meetings, key=lambda e: e[0])
    meeting_rooms = 0
    min_end_heap = []
    for meeting in meetings:
        while min_end_heap and min_end_heap[0][0] <= meeting[0]:
            heapq.heappop(min_end_heap)
        heapq.heappush(min_end_heap, (meeting[1], meeting))
        meeting_rooms = max(meeting_rooms, len(min_end_heap))
    return meeting_rooms


print(min_meeting_rooms([[1, 4], [2, 5], [7, 9]]))
print(min_meeting_rooms([[6, 7], [2, 4], [8, 12]]))
print(min_meeting_rooms([[1, 4], [2, 3], [3, 6]]))
print(min_meeting_rooms([[4,5], [2,3], [2,4], [3,5]]))
