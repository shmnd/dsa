class Solution:
    def arraySign(self, nums: List[int]) -> int:

        negs = 0 

        for x in nums:
            if x == 0:
                return 0 
            elif x < 0:
                negs += 1

        if negs % 2 == 0:
            return 1
        return -1

        