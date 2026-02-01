class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:  # If odd (and not 1), not a power of 2
                return False
            n = n // 2
        
        return True  # Reached 1
        

        