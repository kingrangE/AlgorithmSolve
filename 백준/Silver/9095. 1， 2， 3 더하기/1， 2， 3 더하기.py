d = [0]*11
T = int(input())
targets = []
for i in range(T):
    targets.append(int(input()))
d[0] = 1
for i in range(1,11):
    d[i] = d[i-1] # + 1 하는 경우의 수
    if i >= 2 :
        d[i] += d[i-2] # + 2 하는 경우의 수 추가
    if i >= 3 :
        d[i] += d[i-3] # + 3 하는 경우의 수 추가

for target in targets :
    print(d[target])