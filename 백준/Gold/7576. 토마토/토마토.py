"""
10^6 >= 상자의 크기 > 4 
따라서 O(NlogN) 이하의 시간 복잡도로 수행해야 함.
"익은 토마토"가 들어있는 위치로부터 "상하좌우"가 "하루 뒤에" 익음
1. 전체 큰 while 문 -> 날짜 의미 -
2. 내부 while문 -> queue가 빌 때까지 반복하며 익은 토마토의 위치를 추가함.
3. box의 모든 값이 1 이면 날짜 출력 후 종료, box의 모든 값이 1은 아닌데 변동이 없으면 -1 출력 후 종료
"""

# O(N)
def all_ripe(box:list)->bool:
    for row in box :
        for val in row : 
            if val == 0 :
                return False
    return True
def print_box(box:list):
    for row in box :
        print(row,'\n')


from collections import deque
M,N = list(map(int, input().split()))

box = [list(map(int,input().split())) for _ in range(N)]
q = deque([])
tmp = deque([])

if all_ripe(box) :
    print("0")
    exit(0)

# 초기 애들 위치 넣어주기
for i,row in enumerate(box):
    for j,val in enumerate(row):
        if val == 1 :
            q.append((i,j))

day = 0
dx = [0,0,1,-1]
dy = [-1,1,0,0]

while True:
    q.extend(tmp)
    tmp = deque([])
    while q :
        i,j = q.popleft()
        for mx,my in zip(dx,dy):
            nx,ny = i+mx,j+my # 새로운 위치 갱신
            if 0 <= ny < M and 0 <= nx < N and box[nx][ny] == 0: 
                #유효한 위치라면
                box[nx][ny] = 1 # 표시
                tmp.append((nx,ny)) # 새 익은 토마토 넣기
    if not tmp: # q가 비면 종료 만약 다 채웠으면 여기 오기전에 끝남
        break
    day+=1

if all_ripe(box) :
    print(day)
else :
    print("-1")