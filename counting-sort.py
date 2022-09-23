def counting_sort(numbers, max_value=None):
    if max_value is None:
        max_value = max(numbers)

    count = [0] * (max_value + 1)

    for num in numbers:
        count[num] += 1

    print(count)

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    print(count)

    output = [0] * len(numbers)
    for num in numbers:
        output[count[num] - 1] = num
        count[num] -= 1

    print(output)


if __name__ == "__main__":
    counting_sort([4, 2, 2, 8, 3, 3, 1])
