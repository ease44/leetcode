import operator
from functools import reduce


def test(num):
    if num < 10:
        return num
    num = reduce(operator.add, map(int, str(num)))
    while num // 10 != 0:
        num = reduce(operator.add, map(int, str(num)))
    return num


def test2(num):
    if num == 0:
        return 0
    return (num - 1) % 9 + 1


if __name__ == '__main__':
    print(test(58))
    print(test2(58))
