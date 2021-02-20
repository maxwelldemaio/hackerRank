class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash = {}
        # Create map from first string
        for char in s:
            if char in sHash:
                sHash[char] += 1
            else:
                sHash[char] = 1

        # Compare for same frequency
        for char in t:
            if char in sHash:
                if sHash[char] < 1:
                    return False
                sHash[char] -= 1
            else:
                return False
        return True

# Tests
example = Solution()
print(example.isAnagram(s="anagram", t="nagaram"))
