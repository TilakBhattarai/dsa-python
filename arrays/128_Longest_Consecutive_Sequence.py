class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        maxCount = 0

        for num in nums:
            if not num - 1 in nums:
                count = 1

                while num + 1 in nums:
                    count += 1
                    num += 1
                maxCount = max(maxCount, count)
        return maxCount


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))
