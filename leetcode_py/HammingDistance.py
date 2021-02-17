class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Creates a binary sequence (0's where the same, 1's where different)
        # Example 4^1 would be 5 (since binary 100 and 001 would result in 101)
        result = x^y
        count = 0
        while(result>0):
            print(result)
            count += result & 1
            # Shift bits to the right until we reach the end
            result >>= 1
        return count

# Tests
myExample = Solution()
print(myExample.hammingDistance(6,0))

# 110
# 000

# 110
# 011
# 001
# 000

# 2 places where diff
