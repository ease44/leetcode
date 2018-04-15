"""
testcase:
1 2 -> 0.5
2 3 -> 0.(6)
1 333 -> 0.(003)
"""


def test(numerator, denominator):
    if numerator == 0:
        return '0'
    if numerator < 0 < denominator or denominator < 0 < numerator:
        res = '-'
    else:
        res = ''
    a = abs(numerator)
    b = abs(denominator)
    if a < b:
        res += '0.'
    else:
        res += str(a // b)
        if a % b != 0:
            res += '.'
        else:
            return res
    fractional_dict = {}
    while True:
        y = (a % b) * 10
        if y not in fractional_dict:
            fractional_dict[y] = len(res)
            x = y // b
            res += str(x)
            a = y % b
            if a == 0:
                break
        else:
            res_list = list(res)
            res_list.insert(fractional_dict[y], '(')
            res_list.append(')')
            res = ''.join(res_list)
            break

    return res


if __name__ == '__main__':
    print(test(1, 333))
