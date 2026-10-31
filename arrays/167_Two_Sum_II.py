class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current > target:
                right -= 1
            else:
                left += 1


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
