# coding:utf-8
def findPalid(s):
    if len(s) < 2:
        return s
    res = ''
    for i in range(len(s)):
        left = right = i
        while left >= 0 and right < len(s) and s[right] == s[left]:
            left -= 1
            right += 1
        if right - left - 1 > len(res):
            res = s[left + 1: right]
    return res


if __name__ == '__main__':
    # s = 'abaaa'
    s = 'aa'
    print(findPalid(s))