class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        count = [0, 1]
        index = 0
        flag = 2

        for i in range(2, num+1):
            if i == flag:
                flag *= 2
                index = 0

            count.append(count[index]+1)
            index += 1

        return count


class Solution2:
    def countBits(self, num):
        ret = [0]
        for i in range(1, num + 1):
            # ret[i] = ret[i&(i-1)] + 1;
            ret.append(ret[i&(i-1)]+1)
        return ret

r = Solution2().countBits(10)

print(r)