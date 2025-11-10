from collections import deque

F,S,G,U,D = map(int,input().split())

if S == G:
    print(0)
    exit()

# visited를 -1로 초기화 (미방문 상태)
visited = [-1 for _ in range(F+1)]

q = deque()
q.append(S)
visited[S] = 0 # 시작점은 0번 이동

while q :
    now = q.popleft()
    
    for next in [now+U, now-D]:
        # 1. 범위 체크
        # 2. 미방문 체크 (visited[next] == -1)
        if 1 <= next <= F and visited[next] == -1:
            visited[next] = visited[now] + 1 # 이동 횟수 기록
            q.append(next)
            
            # (최적화) 큐에 넣을 때 G인지 확인하면 더 빠름
            if next == G:
                print(visited[G])
                exit()

# while이 끝날 때까지 G를 못 찾음
print("use the stairs")