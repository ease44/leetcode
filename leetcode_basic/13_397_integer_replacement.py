
def test(n):
    res = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n == 3:  # 特殊情况单独考虑
                res += 2
                break
            elif (n - 1) % 4 == 0:  # 奇变偶后如果除以2还可以是偶数 那么就是最好的选择
                n -= 1
            else:
                n += 1
        res += 1
    return res


def test2(n):
    lookup = {}

    def recurse(v):
        if v == 1:
            return 0
        if v not in lookup:
            if v % 2 == 0:
                lookup[v] = recurse(v // 2) + 1
            else:
                lookup[v] = min(recurse(v + 1), recurse(v - 1)) + 1
        return lookup[v]

    return recurse(n)


if __name__ == '__main__':
    print(test(10))
    print(test2(10))
