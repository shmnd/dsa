class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c = 0 
        costs.sort()
        for i in costs:
            if i > coins:
                break
                 
            coins -= i
            c+=1
        return c
        