"""
testcase:
'' -> 0
'1' -> 1
'+-2' -> 0
'2147483648' -> 2147483647
"""


def test(str=''):
    str = str.lstrip()
    res = 0
    tmp = '0123456789'
    is_negative = 0
    for i in str:
        if i == '-' and not is_negative:  # 这是为了避开+-连起来的情况
            is_negative = -1
        elif i == '+' and not is_negative:
            is_negative = 1
        elif i in tmp:
            res = res * 10 + int(i)
        else:
            break
    if is_negative:
        res = is_negative * res
    if res < -2147483648:
        res = -2147483648
    elif res > 2147483647:
        res = 2147483647
    return res


if __name__ == '__main__':
    print(test('2'))
