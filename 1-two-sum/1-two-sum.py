class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,j in enumerate(nums):
            for value in nums_dict:
                if target - value == j:
                    return(i,nums_dict[value])
            nums_dict[j] = i