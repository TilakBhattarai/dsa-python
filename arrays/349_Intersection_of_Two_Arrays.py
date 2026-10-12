# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         nums1 = set(nums1)
#         nums2 = set(nums2)

#         return nums1 & nums2


# obj = Solution()
# print(obj.intersection([1, 2, 2, 1], [2, 2]))


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


obj = Solution()
print(obj.intersection([1, 2, 2, 1], [2, 2]))
