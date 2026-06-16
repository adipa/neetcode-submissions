class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = None

        for t in tokens:
            match t:
                case '+':
                    temp = stack.pop() + stack.pop()
                    stack.append(temp)
                case '-':
                    temp = -1 * (stack.pop() - stack.pop())
                    stack.append(temp)
                case '*':
                    temp = stack.pop() * stack.pop()
                    stack.append(temp)
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _ :
                    stack.append(int(t))
                
            print(stack)

        return stack.pop()

                
