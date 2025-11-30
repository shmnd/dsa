class Solution:

    def checking(self,num):
        s = 0 
        for i in str(num):
            s += int(i)
        return s 

    def smallestIndex(self, nums: List[int]) -> int:
            
        for i in range(len(nums)):
            if i == self.checking(nums[i]):
                return i
        return -1