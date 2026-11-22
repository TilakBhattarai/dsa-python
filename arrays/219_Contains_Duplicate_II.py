class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        seen = {}

        for index, num in enumerate(nums):
            if num in seen:
                seen[num] = index
                if abs(seen[num] - index) <= k:
                    return True
            seen[num] = index
        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))
