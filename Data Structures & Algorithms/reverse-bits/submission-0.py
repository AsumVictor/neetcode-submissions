class Solution:
    def reverseBits(self, n: int) -> int:
        """
        00000000000000000000000000010101
        for bit == 0
        get the last n bit from right and left
          - mask n from left and check if is 0
          - mask n from right and check if is 0
          if all z0 move

          else if one is not 0:
             set them 

        set the n right and left bit
        increase n
        """
        res = 0
        for i in range(32):
            #
            bit  = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res


