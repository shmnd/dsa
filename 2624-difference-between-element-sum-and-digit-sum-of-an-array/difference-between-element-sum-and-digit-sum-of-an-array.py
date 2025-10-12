class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for i in nums:
            sum1 += i

        for j in nums:
            for k in str(j):
                sum2 += int(k)
 
        return abs(sum1 - sum2)
            






        