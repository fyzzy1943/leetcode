class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        max = nums[0]
        j = 0
        while True:
            if j >= len(nums) or nums[j] > 0:
                break

            if nums[j] > max:
                max = nums[j]
            j += 1

        tmp = 0
        for i in range(j, len(nums)):
            if nums[i] < 0:
                if tmp + nums[i] > 0:
                    tmp += nums[i]
                else:
                    tmp = 0
            else:
                tmp += nums[i]

            if tmp > max:
                max = tmp

        return max



nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [-2, -1]
nums2 = [1,2]
res = Solution().maxSubArray(nums2)
print(res)
