N,X = map(int,input().split())

arr = [i for i in list(map(int,input().split())) if i < X ]
print(*arr)

