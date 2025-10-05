def get_pairs_number(lst: list[int], n: int) -> list[tuple]:
    final_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                final_lst.append((lst[i], lst[j]))
    return final_lst
print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))
