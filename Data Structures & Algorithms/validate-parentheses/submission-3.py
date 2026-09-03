class Solution:
    def isValid(self, s: str) -> bool:
        meow = []
        for l in s:
            if l == "}":
                if len(meow) < 1 or meow.pop() != "{":
                    return False
            elif l == ")":
                if len(meow) < 1 or meow.pop() != "(":
                    return False
            elif l == "]":
                if len(meow) < 1 or meow.pop() != "[" :
                    return False
            else:
                meow.append(l)
        if len(meow) > 0:
            return False
        else:
            return True
            