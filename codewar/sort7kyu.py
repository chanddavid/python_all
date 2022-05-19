def solution(nums):
    
    if nums is None:
        return []
      
    else:
        nums.sort()
        return nums
x=solution([])
print(x)