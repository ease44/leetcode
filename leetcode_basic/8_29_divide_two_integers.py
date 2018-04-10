"""
testcase:
0 1 -> 0
-1 1 -> -1
-1 -1 -> 1
1004958205 -2137325331 -> 0
"""


def test(dividend, divisor):
    if dividend == 0:
        return 0

    res = 0
    if dividend < 0 < divisor or divisor < 0 < dividend:
        diff = -1
    else:
        diff = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    n = 1  # 加速，为了下降的更快一点
    while dividend >= divisor:
        dividend -= divisor * n
        res += n
        n += n
        if dividend < divisor * n:
            n = 1

    if res * diff > 2147483647 or res * diff < -2147483648:
        return 2147483647
    else:
        return res * diff


if __name__ == '__main__':
    print(test(-1, -1))
