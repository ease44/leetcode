"""
testcase:
0 0 0 -> True
0 0 1 -> False
"""


def test(x, y, z):
    if x + y < z:
        return False
    elif x == 0 and y != z:
        return False
    elif x == y == z == 0:
        return True

    # 最大公约数
    while y != 0:
        x, y = y, x % y

    return z % x == 0


if __name__ == '__main__':
    print(test(3, 5, 4))

