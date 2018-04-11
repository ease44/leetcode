
def test(num):
    if num == 1:
        return True
    x = num / 2
    while x * x > num:
        x = int((x + num / x) / 2)

    return x * x == num


def test2(num):
    x = num ** 0.5
    return x == int(x)


if __name__ == '__main__':
    print(test(11))
    print(test2(11))
