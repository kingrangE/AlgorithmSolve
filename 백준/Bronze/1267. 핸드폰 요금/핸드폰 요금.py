N = int(input())
times = list(map(int,input().split()))

Y = sum([ int(time//30+1)*10 for time in times])
M = sum([ int(time//60+1)*15 for time in times])

if Y > M :
    print("M",M)
elif Y == M :
    print("Y M",Y)
else :
    print("Y",Y)