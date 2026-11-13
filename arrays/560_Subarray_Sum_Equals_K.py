# class Solution(object):
#     def subarraySum(self, nums, k):
#         count = 0
#         currentSum = 0

#         prefix_map = {0: 1}

#         for num in nums:
#             currentSum += num

#             needed = currentSum - k

#             if needed in prefix_map:
#                 count += prefix_map[needed]

#             prefix_map[currentSum] = prefix_map.get(currentSum, 0) + 1

#         return count


# obj = Solution()
# print(obj.subarraySum([1, 2, 1, 2], 3))


# class Solution(object):
#     def subarraySum(self, nums, k):
#         count = 0
#         for i in range(len(nums)):
#             currSum = 0
#             for j in range(i, len(nums)):
#                 currSum += nums[j]

#                 if currSum == k:
#                     count += 1
#         return count


# obj = Solution()
# print(obj.subarraySum([1, 1, 1], 2))


class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum = 0
        prefix_map = {0: 1}

        for num in nums:
            currSum += num

            needed = currSum - k

            if needed in prefix_map:
                count += prefix_map[needed]
            prefix_map[currSum] = prefix_map.get(currSum, 0) + 1

        return count


obj = Solution()
print(obj.subarraySum([1, 1, 1], 2))
