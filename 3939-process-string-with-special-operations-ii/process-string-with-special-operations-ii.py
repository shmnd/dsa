class Solution:
    def processStr(self, s, k):

        length = 0
        lens = []

        for ch in s:
            if ch.islower():
                length += 1
            elif ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length *= 2

            lens.append(length)

        if k >= lens[-1]:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            prev = lens[i - 1] if i else 0
            ch = s[i]

            if ch.islower():
                if k == prev:
                    return ch

            elif ch == '#':
                if k >= prev:
                    k -= prev

            elif ch == '%':
                k = prev - 1 - k

        return '.'



            

        