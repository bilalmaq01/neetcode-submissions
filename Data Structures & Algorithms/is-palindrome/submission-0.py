class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(filter(str.isalnum, s))).lower()
        print(s)
        fletterindex = 0
        lletterindex = len(s) - 1 
        for i in range(len(s)//2):
            if fletterindex == lletterindex:
                return True
            if s[fletterindex] == s[lletterindex]:
                fletterindex += 1
                lletterindex -= 1
                continue
            else:
                return False
        return True

        