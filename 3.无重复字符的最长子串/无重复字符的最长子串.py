# coding: utf-8

def lengthOfLongestSubstring(s):
    max_len = 0
    if len(s) == 0 or len(s) == 1:
        max_len = len(s)
    else:
        for i in range(0, len(s) - 1):
            for j in range(1, len(s)):
                if s[j] in s[i:j]:
                    right = j
                    left = i
                    max_len = right - left
                elif j == len(s) - 1:
                    if max_len < j - i + 1:
                        max_len = j - i + 1
    return max_len


if __name__ == '__main__':
    s = 'abcabc'
    print(lengthOfLongestSubstring(s))
