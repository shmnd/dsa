class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxVal = float('-inf')
        curVal = 0 

        for i in nums:
            curVal += i

            if curVal > maxVal:
                maxVal = curVal 

            if curVal < 0 :
                curVal = 0 

        return maxVal


        