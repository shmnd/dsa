class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        res = []

        for i in range(len(nums)-k+1):
            count = Counter(nums[i:i+k]) #hash map

            if len(count) <= x:
                res.append(sum(nums[i:i+k]))

            else:
                pair = list(count.items())

                pair.sort(key=lambda p: (p[1],p[0]),reverse=True)

                cur_sum = 0
                for num,count in pair[:x]:
                    cur_sum += (num*count)

                res.append(cur_sum)

        return res





        


        