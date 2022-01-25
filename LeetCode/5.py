# 5. 最长回文子串

"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""


class Solution:
    # 遍历数组，找到
    @staticmethod
    def longest_palindrome(s: str) -> str:
        max_string = s[0]
        length = len(s)
        s_list = list(s)
        for i, character in enumerate(s_list):
            if i < length - 1 and character == s_list[i + 1]:
                # max_string = solution.find_max_string(s_list, i, i + 1, max_string)
                max_string = Solution.find_max_string(s_list, i, i + 1, max_string)
            if i < length - 2 and character == s_list[i + 2]:
                max_string = Solution.find_max_string(s_list, i, i + 2, max_string)
        return max_string

    @staticmethod
    def find_max_string(s_list, start, end, max_string):
        length = len(s_list)
        while start >= 0 and end < length and s_list[start] == s_list[end]:
            start -= 1
            end += 1
        start += 1
        end -= 1
        if len(max_string) < end - start + 1:
            max_string = ''.join(s_list[start:end + 1])
        return max_string


if __name__ == '__main__':
    string = "ac"
    solution = Solution()
    print(solution.longest_palindrome(string))

