def solution(array, commands):
    answer = []
    for i,j,k in commands :
        tmp = array[i-1:j]
        tmp.sort() # sorted가 return값 있는 정렬인데 기억 안나서 걍 이렇게 함
        answer.append(tmp[k-1])
        
    return answer