class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur =0 
        maz = 0 

        for i in gain:
            cur += i
            maz  = max(maz,cur)

        return maz
        
        