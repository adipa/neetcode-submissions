class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            if stack:
                pos, spd = stack.pop()
                time_curr = (target - p) / s
                time_prev = (target - pos) / spd
                stack.append((pos, spd))
                if time_prev < time_curr:
                    stack.append((p, s))
            else:
                    stack.append((p,s))

        return len(stack)

        