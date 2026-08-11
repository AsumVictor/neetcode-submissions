class Solution:
    def hammingWeight(self, n: int) -> int:
        # return the kahn algo

        count = 0
        number = n

        while number > 0:
            # clear the LSB setbit
            number = number & (number - 1)
            count += 1

        return count
        