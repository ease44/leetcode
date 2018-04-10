

def test(x):
    # 牛顿法
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1

    seed = x
    tmp = x // 3
    while abs(seed - tmp) > 0:
        seed = tmp
        tmp = (seed + x / seed) / 2

    return int(seed)


def test2(x):
    return int((x ** (1/2)))


if __name__ == '__main__':
    print(test(10))
    print(test2(10))
