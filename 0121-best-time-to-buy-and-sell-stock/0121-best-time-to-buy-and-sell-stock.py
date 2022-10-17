class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bef=prices[0]
        pf=0
        for i in prices[1:]:
            if i>bef:
                pf=max(pf,i-bef)
                
            bef=min(bef,i)
            
        return pf