class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        count = 0

        freq = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in freq:
                count += freq[prefix - k]

            if prefix in freq:
                freq[prefix] += 1
            else:
                freq[prefix] = 1

        return count