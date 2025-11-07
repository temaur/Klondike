def get_most_frequent_symbol(s: str) -> tuple[str, int]:
    my_set = {(x, s.count(x)) for x in s}
    if my_set == set():
        return 0
    return sorted(my_set, key=lambda item: item[1])[-1]


assert get_most_frequent_symbol("aaeeaeabenbbbaaaaaaa") == ("a", 11)
assert get_most_frequent_symbol("11111113433434434") == ("1", 7)
assert get_most_frequent_symbol("") == 0
print("All tests passed")