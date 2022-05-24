def find_number_pairs(numbers, N=10):
    tup_list = []
    for count, value in enumerate(numbers):
        for x in numbers[count + 1:]:
            if value + x == N:
                tup_list.append((value, x))

    return tup_list