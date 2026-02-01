class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=set(nums)
        nums.clear()
        for i in x:
            nums.append(i)
        nums.sort()
        return len(nums)
                    
        