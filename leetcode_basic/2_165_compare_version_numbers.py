"""
testcase:
1 < 1.1, 1.0 = 1
"""


def test(version1='1', version2='1.0'):
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    for a, b in zip(version1, version2):  # zip只做到最短的
        if a < b:
            return -1
        elif a > b:
            return 1

    if len(version1) > len(version2):
        for i in version1[len(version2):]:  # 这是是为了把长的后面全是0的情况考虑进去
            if i != 0:
                return 1
        return 0
    elif len(version1) < len(version2):
        for i in version2[len(version1):]:
            if i != 0:
                return -1
        return 0
    else:
        return 0


if __name__ == '__main__':
    print(test())
