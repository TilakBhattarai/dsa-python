# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         maxSum = float("-inf")

#         for i in range(n):
#             currSum = 0
#             for j in range(i, n):
#                 currSum += nums[j]
#                 maxSum = max(maxSum, currSum)
#         return maxSum


# obj = Solution()
# print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currSum = 0
        maxSum = float("-inf")

        for num in nums:
            currSum += num

            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        return maxSum


obj = Solution()
print(obj.maxSubArray(nums=[2, -5, 4, 3]))
