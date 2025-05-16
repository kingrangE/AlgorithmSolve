N = int(input())
d = [0]*N
scores = [int(input()) for _ in range(N)]

if len(scores) <= 2 :
    print(sum(scores))
else :
    d[0] = scores[0]
    d[1] = scores[0]+scores[1]
    for i in range(2,N):
        d[i] = max(scores[i]+scores[i-1]+d[i-3],scores[i]+d[i-2])
    print(d[-1])