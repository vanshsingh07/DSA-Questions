class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}
        count = 0
        maximum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in first:
                maximum = max(maximum, i - first[count])
            else:
                first[count] = i

        return maximum