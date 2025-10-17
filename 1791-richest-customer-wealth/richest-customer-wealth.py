class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in accounts:
            val = 0 
            for j in range(len(i)):
                val += i[j]
                if j+1 == len(i):
                    arr.append(val)

        gv = 0 
        for i in arr:
            if i > gv:
                gv = i
        return gv


        