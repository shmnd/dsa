class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapp = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for i in s:
            if i in mapp:
                top_ele = stack.pop() if stack else '#'
                if mapp[i] != top_ele:
                    return False
            else:
                stack.append(i)

        return not stack