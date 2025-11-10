"""
N 입력
N개의 숫자 입력
T 입력 

N을 최대한 T로 나눠줄 수 있는 숫자 출력

T//N을 구한 후, 계산해야 할듯

O(NlogN)
"""
from collections import deque

N = int(input())
arr = deque(sorted(list(map(int,input().split()))))
T = int(input())

pivot = T//N
sur = T #잉여분
max_v = 0
while arr:
    pivot = int(sur/len(arr))
    if arr[0] > pivot  : # 나눈 값보다 최솟값이 크면
        print(pivot) #나눈 값을 주면 끝
        break
    elif arr[-1] < pivot : # 나눈 값이 최대값보다 크면
        print(arr[-1]) #최대값을 다 줄 수 있으므로 최대값 출력
        break
    if max_v < arr[0] :
        max_v = arr[0]
    sur -= arr[0] # 피봇이 최소보단 크면 최솟값은 다 줄 수 있다는거
    arr.popleft()
if not arr :
    print(max_v)