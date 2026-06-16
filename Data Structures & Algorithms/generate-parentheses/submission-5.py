class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(openC, closeC, sub):
            if openC == closeC == n:
                # result.append("".join(stack))
                result.append(sub)
                return

            if openC < n:
                # stack.append("(")
                backtrack(openC + 1, closeC, sub + "(")
                # stack.pop()

            if closeC < openC:
                # stack.append(")")
                backtrack(openC, closeC + 1, sub + ")")
                # stack.pop()

        backtrack(0,0, "")
        return result
                        