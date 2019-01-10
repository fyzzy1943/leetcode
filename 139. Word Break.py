class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s in wordDict:
            return True

        for i in range(1, len(s)):
            if s[0:i] in wordDict:
                if self.wordBreak(s[i:], wordDict) == True:
                    return True

        return False

    def wordBreak(self, s, wordDict):
        return self._wordBreak(s, wordDict, 0)

    def _wordBreak(self, s, wordDict, start):
        if start == len(s):
            return True

        for word in wordDict:
            newStart = start + len(word)

            if newStart > len(s):
                continue

            if s[start:newStart] == word:
                if self._wordBreak(s, wordDict, newStart) == True:
                    print(word)
                    return True

        return False

    def wordBreak(self, s, wordDict):
        if not s:
            return True

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

    def wordBreak(self, s, wordDict):
        if not s:
            return True

        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            for word in wordDict:
                end = i + len(word)
                if end > len(s):
                    continue

                if dp[end]:
                    continue

                if s[i:end] == word:
                    dp[end] = True

        return dp[len(s)]

# print('abcd'[1:2])
test = 'abcd'
# print(test[0:len(test)+1])

ret1 = Solution().wordBreak('caa', ['a', 'b', 'caa'])
ret2 = Solution().wordBreak('leetcode', ['leet', 'code'])
ret3 = Solution().wordBreak('goalspecial', ["go","goal","goals","special"])
ret4 = Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
print(ret1, ret2, ret3, ret4)
