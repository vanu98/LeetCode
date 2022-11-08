class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        for i in range(0,len(nums)):
            if left == sum(nums[i+1::]):
                return i
            left+=nums[i]
        return -1