from collections import Counter


def freq_query(queries):
    output = list()
    data = Counter()
    rev_data = Counter()

    def add(key):
        prev = data[key]
        data[key] += 1
        rev_data[data[key]] += 1

        if rev_data[prev] > 0:
            rev_data[prev] -= 1

    def sub(key):
        prev = data[key]
        if prev == 0:
            return

        data[key] = prev - 1
        rev_data[data[key]] += 1

        if rev_data[prev] > 0:
            rev_data[prev] -= 1

    def check(amount):
        nonlocal output
        if rev_data[amount] > 0:
            output += [1]
        else:
            output += [0]

    operations = {
        1: add,
        2: sub,
        3: check,
    }

    for q in queries:
        operations[q[0]](q[1])

    return output
