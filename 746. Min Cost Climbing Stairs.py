class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        sum = 0

        while True:
            if len(cost) == 0:
                break
            if len(cost) == 1:
                sum += cost.pop(0)
                break
            left = cost.pop(0)
            right = cost.pop(1)


        return sum

cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

result = Solution().minCostClimbingStairs(cost1)
print(result)
