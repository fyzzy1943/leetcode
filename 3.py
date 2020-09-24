class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        max_count = 0
        count = 1
        now = ''

        for c in s:
            print(now, c, count, max_count)
            if c != now:
                count += 1
            else:
                count = 1
                if count > max_count:
                    max_count = count
            now = c

        if count > max_count:
            max_count = count

        return max_count


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;

a = 'abcabcbb'

substring = Solution().lengthOfLongestSubstring(a)
print(substring)
