class Solution:
    def maximumSubarraySum(self, nums, k):
        count = {}
        left = 0
        total = 0
        ans = 0

        for right in range(len(nums)):
            total += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            # Window size k se bada ho gaya
            if right - left + 1 > k:
                count[nums[left]] -= 1
                total -= nums[left]

                if count[nums[left]] == 0:
                    del count[nums[left]]

                left += 1

            # Exactly k elements + all distinct
            if right - left + 1 == k and len(count) == k:
                ans = max(ans, total)

        return ans