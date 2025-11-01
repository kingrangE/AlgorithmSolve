from collections import deque

N, K = map(int, input().split())
MAX = 100000 # 최대 위치
arr = [0] * (MAX + 1) # 0은 미방문, 0~100000 인덱스

if N == K:
    print(0)
else:
    q = deque([N])
    arr[N] = 1 # 시작점 방문 처리 (0초 + 1 = 1)

    while q:
        x = q.popleft()

        # 세 가지 경우 탐색: x-1, x+1, x*2
        for next_x in (x - 1, x + 1, x * 2):
            # 1. 범위 내에 있고(0 <= next_x <= MAX)
            # 2. 아직 방문하지 않았다면 (arr[next_x] == 0)
            if 0 <= next_x <= MAX and arr[next_x] == 0:
                arr[next_x] = arr[x] + 1 # (이전 시간 + 1) + 1 을 저장
                q.append(next_x)

            # 목적지에 도달했다면 즉시 멈추고 출력
            # (BFS 특성상 K에 처음 도달했을 때가 최단 시간)
            if next_x == K:
                print(arr[K] - 1) # (시간 + 1)이었으므로 -1 해서 출력
                exit() # 프로그램 완전 종료