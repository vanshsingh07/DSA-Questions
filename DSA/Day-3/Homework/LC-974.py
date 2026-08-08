class Solution:
    def subarraysDivByK(self, nums, k):
        prefix = 0
        count = 0

        freq = {0: 1}

        for num in nums:
            prefix += num

            rem = prefix % k

            if rem in freq:
                count += freq[rem]

            if rem in freq:
                freq[rem] += 1
            else:
                freq[rem] = 1

        return count