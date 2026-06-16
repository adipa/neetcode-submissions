class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        water = 0

        while(l < r):

            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])

            if (lMax < rMax):
                water += lMax - height[l]
                l += 1
            else:
                water += rMax - height[r]
                r -= 1

        return water


        