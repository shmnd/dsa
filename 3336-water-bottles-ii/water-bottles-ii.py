class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottle = numBottles
        drunk_bottle = numBottles

        while empty_bottle >= numExchange:
            empty_bottle -= numExchange
            drunk_bottle += 1
            empty_bottle += 1
            numExchange += 1

        return drunk_bottle
        