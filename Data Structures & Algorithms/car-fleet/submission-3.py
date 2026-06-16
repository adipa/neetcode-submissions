class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            if stack:
                pos, spd = stack[-1]
                time_behind = (target - p) / s
                time_ahead = (target - pos) / spd
                if time_behind > time_ahead:
                    stack.append((p, s))
            else:
                    stack.append((p,s))
        return len(stack)

        