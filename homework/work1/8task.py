def is_list_growing(lst: list) -> bool:
    for x in range(len(lst) - 1):
        if lst[x+1] - lst[x] > 0:
            flag = True
        else:
            flag = False
            break
    return flag

assert is_list_growing([0, 1, 3, 4, 7])
assert not is_list_growing([0, 1, 3, 4, 2])
assert not is_list_growing([2, 2, 2, 2, 2])
assert not is_list_growing([4, 3, 2, 1])
print('All tests passed')
