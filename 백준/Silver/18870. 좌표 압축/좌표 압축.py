import bisect
N = int(input())

arr = list(map(int,input().split()))

"""Big O -> O(nlogn)"""

sorted_arr = sorted(list(set(arr)))
result = []
dic = {}
for i,e in enumerate(sorted_arr):
    dic[e] = i

for val in arr:
    result.append(dic[val])

print(*result)