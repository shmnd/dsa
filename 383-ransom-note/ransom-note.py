class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_count = Counter(magazine)

        for i in ransomNote:
            if mag_count[i] > 0:
                mag_count[i] -= 1

            else:
                return False
        return True
        