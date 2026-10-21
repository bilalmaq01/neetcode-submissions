class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max = 1
        maxlength = 0
        mylittledict = {}
        while (right < len(s)):
            if s[right] not in mylittledict:
                mylittledict[s[right]] = 1
            else:
                mylittledict[s[right]] += 1
            if mylittledict[s[right]] > max:
                max = mylittledict[s[right]]
            if max + k >= len(s[left:right+1]) and len(s[left:right+1]) > maxlength:
                maxlength = len(s[left:right+1])
            else:
                mylittledict[s[left]] -= 1
                left += 1
            right += 1
        return maxlength