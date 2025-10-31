class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        arr =[]
        dic = {}

        for i in nums:
            dic[i] = dic.get(i,0)+1

            if dic[i] > 1:
                arr.append(i)

        return arr
        