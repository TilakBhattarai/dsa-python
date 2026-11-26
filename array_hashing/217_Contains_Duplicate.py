class Solution(object):
    def containsDuplicate(self, nums):
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        for key in dictionary:
            if dictionary[key] > 1:
                return True
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))


class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))
