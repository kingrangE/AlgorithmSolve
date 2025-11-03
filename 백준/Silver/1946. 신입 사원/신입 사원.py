"""
테스트 케이스 개수 입력
각 테스트 케이스에 대해
N 입력
r_s,i_s N개 입력 받음
O(NlogN)시간에 해야함
"""
# 1 4
# 2 5 x
# 3 6 x
# 4 2 
# 5 7 x
# 6 1
# 7 3 x

T = int(input())

for _ in range(T):
    N = int(input())
    count = 1
    s = sorted([list(map(int,input().split())) for _ in range(N)])
    min_i_s = s[0][1]
    for _,i_s in s :
        if min_i_s > i_s :
            min_i_s = i_s
            count+=1
    print(count)