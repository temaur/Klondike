def is_list_growing(lst: list) -> bool:
    for x in range(len(lst) - 1):
        if lst[x+1] - lst[x] > 0:
            flag = True
        else:
            flag = False
            break
    return flag

print(is_list_growing([0,1,3,4,7]))
print(is_list_growing([0,1,3,4,2]))
print(is_list_growing([2,2,2,2,2]))
print(is_list_growing([4,3,2,1]))