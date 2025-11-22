class Solution:
    def mySqrt(self, x: int) -> int:

        left = 1
        right = x//2
        res = 0
        
        if x < 2:
            return x 


        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid*mid < x:
                res = mid
                left = mid+1

            else:
                right = mid-1
                
        return res

        

        

        
