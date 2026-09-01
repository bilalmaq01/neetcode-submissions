class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cunt = []
        for op in operations:
            if op == "D":
                cunt.append(cunt[len(cunt)-1] * 2)
            elif op == "C":
                    cunt.pop()
            elif op == "+":
                cunt.append(cunt[len(cunt)-1] + cunt[len(cunt)-2])
            else:
                cunt.append(int(op))
                
        return sum(cunt)

                 