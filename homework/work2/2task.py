# Решение в два списка
def move_zeros(lst: list) -> list:
    zero_cnt = lst.count(0)
    new_lst = [x for x in lst if x != 0]
    new_lst += [0] * zero_cnt
    return new_lst


assert move_zeros([0, 4, 3, 0, 1, 0]) == [4, 3, 1, 0, 0, 0]
assert move_zeros([1, 1, 3, 2, 1, 1]) == [1, 1, 3, 2, 1, 1]
assert move_zeros([0, 0, 0]) == [0, 0, 0]
assert move_zeros([0, 4, 3, 0, 0, 0]) == [4, 3, 0, 0, 0, 0]
assert move_zeros([]) == []
assert move_zeros([1]) == [1]
print('All tests passed')

# Решение с одним исходным списком
def move_zeros2(lst: list)-> list:
    zero_cnt = lst.count(0)
    lst = list(filter(lambda x: x != 0, lst))
    lst += [0] * zero_cnt
    return lst

assert move_zeros2([0, 4, 3, 0, 1, 0]) == [4, 3, 1, 0, 0, 0]
assert move_zeros2([1, 1, 3, 2, 1, 1]) == [1, 1, 3, 2, 1, 1]
assert move_zeros2([0, 0, 0]) == [0, 0, 0]
assert move_zeros2([0, 4, 3, 0, 0, 0]) == [4, 3, 0, 0, 0, 0]
assert move_zeros2([]) == []
assert move_zeros2([1]) == [1]
print('All tests passed')