"""
K N 입력받음
K개의 숫자리스트 입력 받음

K개의 숫자들을 일정한 숫자로 나눈 몫의 합이 N이 되도록하는 가장 큰 숫자를 구하라.

N은 항상 K 이상
따라서 최솟값을 가장 작은 숫자로 받기 -> 가장 작은 숫자로 나누면 무조건 N개 이상이 나옴
init -> 가장 작은 숫자
숫자를 반으로 줄여가며 적절한 숫자 구하기
"""

K,N = map(int,input().split())
nums = [int(input()) for _ in range(K)]

upper = max(nums) # 초기값 
lower = 1 # 상방 한계선 
result = 0
while upper >= lower :
    mid = (upper+lower)//2
    count = sum(x // mid for x in nums)
    # print(f"({upper}+{lower})//2 = {mid}, count = {count}")
    if count >= N :
        lower = mid + 1
    else :
        upper = mid - 1

print(upper)