class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for x in range(32):
            # Leftshift output
            output <<= 1
            # Extract lowest bit of n
            if n & 1:
                output += 1
            n >>= 1
        return output