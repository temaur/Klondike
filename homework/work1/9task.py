def get_pairs_number(lst: list[int], n: int) -> list[tuple]:
    final_lst = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                final_lst.add(tuple(sorted((lst[i], lst[j]))))
    return list(final_lst)


assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [(2, 5), (3, 4)]
assert get_pairs_number([1, 3, 3, 2, 4, 5], 6) == [(2, 4), (3, 3), (1, 5)]
assert get_pairs_number([1, 3, 3, 2, 4, 5], 1) == []
assert get_pairs_number([5, 5, 5, 5], 10) == [(5, 5)]
print("All tests passed")


""" Но изначально я решил так
def get_pairs_number(lst: list[int], n: int) -> list[tuple]:
    final_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                final_lst.append((lst[i], lst[j]))
    return final_lst
print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))
"""
