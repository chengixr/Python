# 1220. 统计元音字母序列的数目

"""
给你一个整数n，请你帮忙统计一下我们可以按下述规则形成多少个长度为n的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音'a'后面都只能跟着'e'
每个元音'e'后面只能跟着'a'或者是'i'
每个元音'i'后面不能 再跟着另一个'i'
每个元音'o'后面只能跟着'i'或者是'u'
每个元音'u'后面只能跟着'a'
由于答案可能会很大，所以请你返回 模10^9 + 7之后的结果。
"""


class Solution:
    @staticmethod
    def count_vowel_permutation(n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = (
                (dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007,
                (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007
            )
        return sum(dp) % 1000000007


if __name__ == '__main__':
    num = 5
    solution = Solution()
    print(solution.count_vowel_permutation(num))
