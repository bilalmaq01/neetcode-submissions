class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        norep = set()
        l = 0
        maxlen = 0

        for r in range(len(s)):
            while s[r] in norep:
                norep.remove(s[l])
                l += 1
            norep.add(s[r])
            maxlen = max(maxlen, r-l + 1)
        return maxlen