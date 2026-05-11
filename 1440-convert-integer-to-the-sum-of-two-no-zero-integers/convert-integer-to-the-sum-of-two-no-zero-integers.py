class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def check(val):
            return '0' not in str(val)

        for i in range(1,n):
            j = n-i
            if check(i) and check(j):
                return [i,j]
        