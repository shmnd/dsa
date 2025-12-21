class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            sqr = abs(nums[i]*nums[i])

            nums[i] = sqr

        nums.sort()

        return nums
        