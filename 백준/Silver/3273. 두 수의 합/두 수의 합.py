"""
N입력
N개의 자연수 띄어쓰기 구분 입력
목표 숫자 입력

N개의 숫자들 중 두개의 합이 목표 숫자인 쌍의 개수 출력하라.

정렬 -> O(NlogN)
이진탐색 -> O(logN) 
"""

N = int(input())
arr = sorted(list(map(int,input().split())))
X = int(input())
count = 0
for num in arr :
    s = 0 
    e = N-1
    target = X-num
    if target < 0 : # 음수는 입력 받지 않으므로
        continue
    
    while s <= e: # 유효 인덱스 동안 반복
        mid = (s+e)//2 # 중앙 인덱스
        if target == arr[mid] :
            # 쌍을 찾았으면
            count += 1
            break
        elif target < arr[mid] :
            # 타겟보다 크면 작은 부분을 찾아야 함.
            e = mid - 1
        else :
            # 타겟보다 작으면 큰 부분을 찾아야 함.
            s = mid + 1
print(count//2)