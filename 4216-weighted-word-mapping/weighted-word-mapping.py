class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:   
        result = []

        for word in words:
            total_weight = 0

            for ch in word:
                total_weight += weights[ord(ch) - ord('a')]

            mod_val = total_weight % 26

            # Reverse alphabetical mapping:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped_char = chr(ord('z') - mod_val)

            result.append(mapped_char)

        return "".join(result)