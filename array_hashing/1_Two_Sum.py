# Brute Force (o(n2))
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))

# Hashmap Optimal(o(n))


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
