class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)-nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val :
                nums[i] = -1
        nums.sort(reverse=1)
        return k