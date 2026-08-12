class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans