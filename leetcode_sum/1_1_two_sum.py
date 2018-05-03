

def test(nums, target):
    items = {}
    for i, e in enumerate(nums):
        if e in items:
            return [items[e], i]
        items[target - e] = i


if __name__ == '__main__':
    print(test([2, 7, 11, 15], 9))
