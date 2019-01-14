class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        #
        # nums.sort()
        # lens = len(nums)
        # for i in range(0, len(nums) - 2):
        #     for j in range(i+1, lens-1):
        #         for k in range(j+1, lens):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 # print(i, j, k)
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 # tmp.sort()
        #                 # print(tmp)
        #                 if tmp not in res:
        #                     res.append(tmp)
        #
        # return res

        nums.sort()
        res = []
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return res

# print(range(2, 4))
test1 = [-1,0,1,2,-1,-4]
print(test1)
print(Solution().threeSum(test1))

test2 = [-1,0,1,8,-4,-4,-4, 8, 8]
print(test2)
print(Solution().threeSum(test2))
