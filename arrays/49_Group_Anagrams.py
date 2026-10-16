class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}

        for text in strs:
            key = "".join(sorted(text))

            if key not in anagram:
                anagram[key] = []

            anagram[key].append(text)

        return list(anagram.values())


obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
