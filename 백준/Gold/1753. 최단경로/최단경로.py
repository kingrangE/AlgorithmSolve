import heapq
import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

# 1. 인접 리스트 자료구조 생성
# graph[u] = [(v, w), (v', w'), ...]
# u에서 v로 가는 가중치 w의 간선
graph = [[] for _ in range(V + 1)]

# 2. 비용(cost) 배열 초기화
# 모든 비용을 무한(infinity)으로 설정
cost = [float('inf')] * (V + 1)

# 3. 간선 정보 입력받아 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # u에서 v로 가는 가중치 w

def dijkstra(start):
    # 우선순위 큐 (최소 힙)
    # (비용, 정점 번호) 순서로 저장
    q = []
    
    # 1. 시작 노드 초기화
    cost[start] = 0
    heapq.heappush(q, (0, start)) # (비용 0, 시작노드 K)

    while q: # 큐가 비어있지 않은 동안 반복
        # 2. 비용이 가장 적은 노드를 꺼냄
        current_cost, current_node = heapq.heappop(q)
        
        # 3. 이미 처리된 노드인지 확인 (최적화)
        # 큐에서 꺼낸 비용이 이미 저장된 비용보다 크다면
        # 이전에 더 짧은 경로로 방문했다는 뜻이므로 무시
        if cost[current_node] < current_cost:
            continue
            
        # 4. 현재 노드와 연결된 이웃 노드들 확인
        for neighbor_node, neighbor_weight in graph[current_node]:
            # 5. 현재 노드를 거쳐 이웃 노드로 가는 새로운 비용 계산
            new_cost = current_cost + neighbor_weight
            
            # 6. 새로운 비용이 기존 비용보다 짧다면
            if new_cost < cost[neighbor_node]:
                # 7. 비용 갱신
                cost[neighbor_node] = new_cost
                # 8. 큐에 (새 비용, 이웃 노드) 추가
                heapq.heappush(q, (new_cost, neighbor_node))

# 다익스트라 알고리즘 실행
dijkstra(K)

# 결과 출력
for i in range(1, V + 1):
    if cost[i] == float('inf'):
        print("INF")
    else:
        print(cost[i])