from collections import deque


def test(a, b):
    a = list(map(int, a[::-1]))
    b = list(map(int, b[::-1]))
    res = deque()
    m = 0
    for i in range(max(len(a), len(b))):
        ia = a[i] if i < len(a) else 0
        ib = b[i] if i < len(b) else 0
        x = ia + ib + m
        if x == 2:
            x = 0
            m = 1
        elif x > 2:
            x = 1
            m = 1
        else:
            m = 0
        res.appendleft(str(x))
    if m == 1:
        res.appendleft('1')
    return ''.join(res)


def test2(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    print(test('1111', '1111'))
    print(test2('1111', '1111'))
