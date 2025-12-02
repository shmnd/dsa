class Solution:
    def reverseWords(self, s: str) -> str:
        res = []

        last_space_idx = -1

        for i in range(len(s)):

            if i == len(s)-1 or s[i]== ' ':
                space_needed = i if i == len(s)-1 else i-1

                while space_needed > last_space_idx:
                    res.append(s[space_needed])
                    space_needed -= 1

                if i != len(s)-1:
                    res.append(' ')
                last_space_idx = i 

        return ''.join(res)