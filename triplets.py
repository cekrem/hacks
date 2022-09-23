from collections import Counter

nums = [1, 5, 5, 25, 125]
ratio = 5


def count_triplets(arr, r):
    v2 = Counter()
    v3 = Counter()
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1

    return count


print(count_triplets(nums, ratio))
