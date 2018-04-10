"""
testcase:
34.00515 -3 -> 0.00003
"""


def test(x, n):
    sign = 0
    if n == 0:
        return 1
    elif n < 0:
        sign = 1
        n = abs(n)
    m = 1
    while n // 2 != 0:
        if n % 2 == 1:
            m *= x
        x *= x
        n //= 2

    if sign:
        return 1 / x / m
    else:
        return x * m


def test2(x, n):
    return x ** n


if __name__ == '__main__':
    print(test(34.00515, -3))
    print(test2(34.00515, -3))
