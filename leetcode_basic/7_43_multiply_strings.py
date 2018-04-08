"""
testcase:
'0' '0' -> '0'
'123' '456' -> '56088'
'123456789' '987654321' -> '121932631112635269'
"""


def test(num1, num2):
    # 206ms
    if len(num1) == len(num2) == 0:
        return '0'
    tmp_list = [0] * (len(num1) + len(num2))
    for i in range(len(num2) - 1, -1, -1):
        for j in range(len(num1) - 1, -1, -1):
            product = int(num2[i]) * int(num1[j])
            tmp_list[i + j + 1] += product  # 处理相加后的进位问题
            tmp_list[i + j] += tmp_list[i + j + 1] // 10
            tmp_list[i + j + 1] %= 10

    res_list = []
    for x in tmp_list:
        if not res_list and x == 0:
            continue
        else:
            res_list.append(str(x))

    return ''.join(res_list) if res_list else '0'


def test2(num1, num2):
    # 40ms
    return str(int(num1) * int(num2))


if __name__ == '__main__':
    print(test('123456789', '987654321'))
    print(test2('123456789', '987654321'))


