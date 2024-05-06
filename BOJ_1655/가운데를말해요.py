import sys; sys.stdin.readline
import heapq

left_heap = []
right_heap = []

n = int(input())

for _ in range(n):
    m = int(input())
    
    if (len(left_heap) == 0):
        heapq.heappush(left_heap, -m)
    elif(len(right_heap) ==0):
        heapq.heappush(right_heap,m)
    else:
        if(-left_heap[0] < m):
            heapq.heappush(right_heap, m)
        else:
            heapq.heappush(left_heap, -m)
    print(-left_heap[0])
