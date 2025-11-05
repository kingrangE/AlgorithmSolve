import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(input()) for _ in range(M)]

# cost 배열을 M x N 크기로 초기화 (N, M 순서 주의)
cost = [[float('inf')] * N for _ in range(M)] 

q = []
# (비용, x, y) 순서로 heapq에 push
heapq.heappush(q, (0, 0, 0)) 
cost[0][0] = 0 # 시작점 비용 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    # 현재 가장 비용이 적은 노드 정보
    c, x, y = heapq.heappop(q)

    # 1. (메모리 최적화) 
    # 만약 현재 큐에서 꺼낸 비용(c)이 이미 
    # cost 배열에 저장된 값보다 크다면, 
    # 더 이전에 처리된 더 좋은 경로가 있다는 뜻이므로 스킵.
    if c > cost[x][y]:
        continue

    # 2. 도착점 확인 (선택적 최적화)
    # if x == M - 1 and y == N - 1:
    #     print(c)
    #     sys.exit(0) # 프로그램 종료

    for mx, my in zip(dx, dy):
        nx, ny = mx + x, my + y

        if 0 <= nx < M and 0 <= ny < N: # M, N 순서 주의
            # 다음 노드로 가는 새로운 비용 계산
            new_cost = c
            if maps[nx][ny] == '1': # 벽이면 비용 1 추가
                new_cost += 1
            
            # 3. (핵심)
            # 새로운 경로의 비용(new_cost)이 
            # 기존에 저장된 비용(cost[nx][ny])보다 작으면 갱신
            if new_cost < cost[nx][ny]:
                cost[nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny))

print(cost[M-1][N-1]) # M, N 순서 주의