class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                ")": "(",
                "]": "[",
                "}": "{"
            }
        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                else:
                    if stack[-1]==pairs[s[i]]:
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True
        else:
            return False
