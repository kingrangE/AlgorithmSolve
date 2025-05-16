import sys
import heapq
N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(sys.stdin.readline()))
    
total = 0
while len(hq)>1 :
    tmp = heapq.heappop(hq)+heapq.heappop(hq) 
    heapq.heappush(hq, tmp)
    total += tmp

print(total)