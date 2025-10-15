"""
Input : 단어의 개수, 단어들
Output : 그룹단어의 개수

* 그룹단어 -> 단어에 존재하는 모든 문자에 대해, 연속해서 나타나는 경우 
"""

# input
N = int(input())
words = [list(input()) for _ in range(N)]

result = 0
# Module 1
# 각 단어들 반복
for word in words :
    idx = 0 # idx 초기화
    unique_ch = [] # 단어의 고유 문자 저장하는 리스트 초기화
    while idx < len(word) : # 전체 인덱스 반복
        now_ch = word[idx] # 단어의 문자 get
        if now_ch not in unique_ch : # 문자가 list모음에 없다면
            unique_ch.append(now_ch) # 추가
            # 문자가 안 나올때까지 idx 증가
            while idx < len(word) and word[idx] == now_ch :
                idx += 1
        else : # 이미 있는 문자라면 순서 엇갈린 것
            break # 종료
    if idx == len(word): #끝까지 돌았다면 그룹단어
        result += 1
    
print(result)