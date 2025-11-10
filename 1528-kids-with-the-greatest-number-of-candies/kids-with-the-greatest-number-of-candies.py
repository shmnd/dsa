class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        lar = max(candies)
        
        for i in range(0,len(candies)):
            total_candies = candies[i] + extraCandies
            if total_candies >= lar:
                res.append(True)
            else:
                res.append(False)
        return res
