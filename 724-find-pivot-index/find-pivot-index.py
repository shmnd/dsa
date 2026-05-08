class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = 0

        for i , k in enumerate(nums):
            if left_sum == total_sum - left_sum - k:
                return i 
                
            left_sum += k

        return -1
