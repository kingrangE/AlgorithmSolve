def solution(targets):
    targets.sort(key=lambda x:x[1])
    
    criteria = 0
    answer = 0
    
    for start,end in targets :
        if criteria <= start :
            answer += 1
            criteria = end-0.1
            
    return answer