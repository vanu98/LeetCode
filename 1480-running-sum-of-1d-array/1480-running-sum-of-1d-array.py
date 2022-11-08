class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        j=0
        for i in nums:
            j+=i
            arr.append(j)
        return arr