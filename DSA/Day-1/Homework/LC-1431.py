class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        ans = []

        for candy in candies:
            if candy + extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans