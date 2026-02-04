class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0 
        canidate = None 

        for i in nums:
            if count == 0:
                canidate = i 

            count  += (1 if i == canidate else -1 )

        return canidate