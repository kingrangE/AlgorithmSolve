N,M = map(int,input().split())

A = [ list(map(int,input().split())) for _ in range(N)]
B = [ list(map(int,input().split())) for _ in range(N)]

result = [ [x+y for x,y in zip(X,Y)] for X,Y in zip(A,B)]
for nums in result:
    print(*nums, sep=" ")
    