class Solution:
    def maxFreqSum(self, s: str) -> int:

       mapp = Counter(s)
       vowel = max((mapp[i] for i in mapp if i in "aeiou"),default = 0)
       consonant = max((mapp[i] for i in mapp if i not in "aeiou"),default = 0)
       return vowel+consonant

        