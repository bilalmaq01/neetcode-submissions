class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max = 1
        maxlength = 0
        mylittledict = {}
        while (right < len(s)):
            cum = s[right]
            if cum not in mylittledict:
                mylittledict[cum] = 1
            else:
                mylittledict[cum] += 1

            if mylittledict[cum] > max:
                max = mylittledict[cum]

            if max + k >= right + 1 - left and right + 1 - left > maxlength:
                maxlength = right + 1 - left
            else:
                mylittledict[s[left]] -= 1
                left += 1
            right += 1
        return maxlength