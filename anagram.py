from collections import Counter

test_str = "ifailuhkqq"
expected_count = 3

if __name__ == "__main__":
    anagrams = 0
    c = Counter()
    for sub_len in range(1, len(test_str)):
        print(f"sub_len:{sub_len}")
        for start_pos in range(len(test_str) - sub_len + 1):
            sub = "".join(sorted(test_str[start_pos:start_pos + sub_len]))
            c.update([sub])
            print(f"sub: {sub}")
            print(f"counter[sub]: {c[sub]}")
            anagrams += c[sub] - 1

    print(anagrams)

    exit(0)
    second_count = 0
    for v in c.values():
        second_count += v - 1

    print(second_count)

    exit(0)

    chunks = (["".join(sorted(test_str[j:j + i])) for j in range(len(test_str) - i + 1)] for i in
              range(1, len(test_str)))

    c = Counter()
    for chunk in chunks:
        c.update(chunk)

    anagrams = 0
    for sub in c.most_common():
        if sub[1] < 2:
            break
        anagrams += sub[1] - 1

    print(anagrams)
