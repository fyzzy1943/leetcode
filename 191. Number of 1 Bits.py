import time

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1 << 32
        count = 0

        while n > 0:
            if n >= i:
                count += 1
                n -= i
            i >>= 1

        return count

testData = 11

# print(1<<32)
res = Solution().hammingWeight(testData)

print(res)
