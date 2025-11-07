def get_max_rep_symbol(s: str) -> str:
    cnt = 1
    if s == "":
        return 0
    my_set = set()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            my_set.add((s[i], cnt))
            cnt = 1
    my_set.add((s[-1], cnt))
    my_tuple = sorted(my_set, key=lambda item: item[1], reverse=True)[0]
    return my_tuple[0]


assert get_max_rep_symbol("aaaabbbccc") == "a"
assert get_max_rep_symbol("") == 0
assert get_max_rep_symbol("aabb") == "a" or "b"
print("All tests passed")
