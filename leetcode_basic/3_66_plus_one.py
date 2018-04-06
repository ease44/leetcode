"""
给一个整数数组，然后把它当做一个整数，进行+1，得到新的数组，要考虑到进位

testcase:
[1, 0, 1, 1] -> [1, 0, 1, 2]
[1, 0, 9, 9] -> [1, 2, 0, 0]
[9, 9, 9, 9] -> [1, 0, 0, 0, 0]
"""


def test(digits=None):
    t = map(str, digits)
    t = ''.join(t)
    t = int(t) + 1
    t = str(t)
    t = list(map(int, t))
    return t


if __name__ == '__main__':
    print(test([1, 2, 3]))
