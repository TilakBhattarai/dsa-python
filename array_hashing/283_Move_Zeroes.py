class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)

        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))
