"""
testcase:
1 -> 0
0 -> 0
2 -> 0
3 -> 1
"""


def test(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    p_list = [True] * n
    p_list[0] = False
    p_list[1] = False  # 1不是质数
    for i in range(2, int(n ** 0.5) + 1):
        if p_list[i]:
            # for j in range(i * i, n, i):
            #     p_list[j] = False

            # 这比上面用for要快
            p_list[i * i: n: i] = [False] * len(p_list[i * i: n: i])
    return p_list.count(True)


if __name__ == '__main__':
    print(test(60))
