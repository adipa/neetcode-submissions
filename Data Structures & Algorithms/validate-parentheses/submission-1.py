class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if stack:
                    if char == ")":
                        top = stack.pop()
                        if top != "(":
                            return False
                    if char == "}":
                        top = stack.pop()
                        if top != "{":
                            return False
                    if char == "]":
                        top = stack.pop()
                        if top != "[":
                            return False
                else:
                    return False

        return not len(stack)

        