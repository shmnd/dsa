class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n

        a = 1
        b = 1

        for i in range(n-1):

            c = a
            a = a+b
            b = c 

        return a
        

        

        
        