from collections import Counter

input = [1, 1, 2, 4, 2, ]


def solve(arr):
    pairs = 0
    c = Counter(arr)
    for num, occ in c.items():
        print(num, occ)
        c[num] -= occ
        print(c)
        pairs += (occ-1) + c.total()
        print(c.total())
    return pairs


if __name__ == "__main__":
    print(solve(input))
