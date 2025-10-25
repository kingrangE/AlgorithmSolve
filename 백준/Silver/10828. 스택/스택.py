s = []
n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        s.append(order[1])
    elif order[0] == 'top':
        if s:
          print(s[-1])
        else :
          print(-1)
    elif order[0] == 'pop':
        if s :
          print(s.pop())
        else :
          print(-1)
    elif order[0] == 'empty':
        print(0 if s else 1)
    else :
        print(len(s))
