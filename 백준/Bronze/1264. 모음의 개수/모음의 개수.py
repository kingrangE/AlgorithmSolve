모음 = ["a","e","i","o","u"]
result = []

while True:
    string = input()
    tmp = 0
    if string == "#":
        break
    for ch in string:
        if ch.lower() in 모음 :
            tmp += 1
    result.append(tmp)
print(*result,sep="\n")