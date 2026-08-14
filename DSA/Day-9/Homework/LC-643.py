class Solution:
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        maxSum = total

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]

            maxSum = max(maxSum, total)

        return maxSum / k