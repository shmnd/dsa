class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(i) for i in s]

        while len(arr) > 2:

            sec_arr = []

            for j in range(len(arr)-1):
                val = (arr[j] + arr[j+1]) % 10
                sec_arr.append(val)

            arr = sec_arr
                    
        if arr[0] == arr[1]:
            return True
        else:
            return False
            

        