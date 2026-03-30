class Solution:

    def numberOfMatches(self, n: int) -> int:
        # return n-1

        n_match = 0 

        while n > 1:
            match = n // 2
            n_match += match 
            n -= match 

        return n_match


   
   