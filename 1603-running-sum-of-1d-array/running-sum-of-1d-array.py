class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        val = 0 
        for i in range(len(nums)):

            val += nums[i]

            nums[i] = val

        return nums

        