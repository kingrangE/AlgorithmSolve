N = int(input())

nums = list(map(int,input().split()))
nums.sort()

left = 0
right = N-1

answer = abs(nums[left] + nums[right])
final = [nums[left],nums[right]]

while left < right:
    l_value = nums[left]
    r_value = nums[right]

    if abs(l_value+r_value) <answer : 
        final = [l_value,r_value]
        answer = abs(l_value+r_value)
    
        if answer == 0 :
            break
    
    if l_value+r_value > 0 :
        right-= 1
    else : 
        left += 1

print(*final)