class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}

        if len(s) != len(t):
            return False

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1

            if count[ch] < 0:
                return False
        return True


obj = Solution()
print(obj.isAnagram("rat", "car"))
