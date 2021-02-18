from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            # Append if same
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            # We should move forward one pointer if less than other one
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


# Tests
example = Solution()
print(example.intersect([1,1,2,2,5], [2,2,4,3]))