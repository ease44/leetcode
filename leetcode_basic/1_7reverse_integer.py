
def test(x=-123):
    """
    当作字符串处理
    :param x:
    :return:
    """
    if -2147483648 <= x <= 2147483647:
        s = str(x)
        if s[0] == '-':
            a = 0 - int(s[:0:-1])
        else:
            a = int(s[::-1])
        if -2147483648 <= a <= 2147483647:
            return a
        else:
            return 0
    else:
        return 0


def test3(x=1534236469):
    if -2147483648 <= x <= 2147483647:
        if x < 0:
            x = -x  # 这里做转换是躲避python对负数取余时的问题
            is_negative = True
        else:
            is_negative = False

        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
            if x > 2147483648:
                return 0
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            if is_negative:
                return -res
            else:
                return res
    else:
        return 0


if __name__ == '__main__':
    print(test())
    print(test3())
