"""
SCON,SCCC < 가 모두 들어있어야 한 개
N + S = 3개 필요
C = 6개 필요

O -> C C
C C -> O
S -> N
N -> S

"""

S,C,O,N = map(int,input().split())
a = {
    "S" : S + N,
    "C" : C + O*2
}
count = 0
while a["S"]>=3 and a["C"]>=6 :
    a["S"] -= 3
    a["C"] -= 6
    count += 1

print(count)