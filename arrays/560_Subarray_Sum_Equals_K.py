class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currentSum = 0

        prefix_map = {0: 1}

        for num in nums:
            currentSum += num

            needed = currentSum - k

            if needed in prefix_map:
                count += prefix_map[needed]

            prefix_map[currentSum] = prefix_map.get(currentSum, 0) + 1

        return count


obj = Solution()
print(obj.subarraySum([1, 2, 1, 2], 3))
