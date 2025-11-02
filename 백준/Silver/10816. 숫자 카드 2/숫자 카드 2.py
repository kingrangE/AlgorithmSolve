"""
정수 N과 N개의 숫자 주어짐
정수 M과 M개의 숫자 주어짐

N개의 숫자 리스트에서 M개의 숫자 각각이 몇개 있는지를 반환
"""

import sys
N = int(input())

s = sys.stdin.readline
have = list(map(int,s().split()))

M = int(input())
nums = list(map(int,s().split()))

sorted_have = sorted(have)
num_count = {}
for num in sorted_have : 
    num_count[num] = num_count.get(num, 0)+1
def binary_search(have:list,num_count:dict,target:int,s:int,e:int):
    if target not in num_count: 
            # 없으면 종료
            return 0 
    while s<=e:
        mid = (s+e)//2
        if have[mid] == target:
            # 있으면 탐색
            return num_count[target]
        elif have[mid] > target: 
            # 더 작은쪽 탐색 필요
            e = mid -1
        else :
            # 더 큰 쪽 탐색 필요
            s = mid + 1

for num in nums:
    print(binary_search(sorted_have,num_count,num,0,len(sorted_have)-1),end=" ")