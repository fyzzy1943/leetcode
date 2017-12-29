class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)-1
        def costSum(i, j):
            if i == n or i == n-1:
                return cost[i]

            if cost[i] < cost[j]:
                return cost[i] + costSum(i+2, j+2)
            else:
                return cost[j] + costSum(i + 2, j + 2)
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
