"""
N, M이 주어짐
숫자 리스트가 주어짐

1. 절단기의 최대 높이 = 20, 최소 = 0
2. 절단기 상방 하방 /2 를 기준으로 가져가는 나무 길이 계산
    a. 목표보다 크다면? 상방을 낮춤
    b. 목표보다 작다면? 하방을 높임
3. 상방 >= 하방 인 동안 반복 
"""
import sys
s = sys.stdin.readline
N, M = map(int,s().split())
arr = list(map(int,s().split()))

upper = max(arr) # O(N)
lower = 0 
result = 0

while upper >= lower:

    mid = (upper+lower)//2
    cutted_len =sum( i for i in map(lambda x: x-mid, arr) if i > 0 ) # 잘린 길이 계산

    if cutted_len == M : # 딱 댐이면
        result = mid
        break

    elif cutted_len < M : # 목표보다 작으면 더 잘라야 함. upper를 땡겨 더 자름
        upper = mid - 1

    else :
        # 목표보다 크면 덜 잘라야 함. lower를 땡겨 덜 자름
        result = mid
        lower = mid + 1

print(result)