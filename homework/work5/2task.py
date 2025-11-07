def contains_in_list(small: list[int], big: list[int]) -> bool:
    lst = [x for x in big if x in small]
    return lst == small


small = [3, 4, 8, 10]
big = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


assert contains_in_list(small, big)
assert not contains_in_list([3, 4, 8, 1], big)
print("All tests passed")
