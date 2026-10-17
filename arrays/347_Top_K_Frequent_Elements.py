class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_freq = sorted(frequency, key=frequency.get, reverse=True)

        return sorted_freq[:k]


obj = Solution()
print(obj.topKFrequent([2, 2, 1, 1, 1, 3], 2))
