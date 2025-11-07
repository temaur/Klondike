def has_black_list_words(input_str: str, black_list: list[str]) -> bool:
    list_of_occurrences = [True if elem in input_str.lower() else False for elem in black_list]
    return any(list_of_occurrences)


input_str = "У попа была собака, он ее любил"
black_list = ["собака", "кот", "мышь"]


assert has_black_list_words(input_str, black_list)
assert has_black_list_words("Это была необычная мышь, ее Звали Стюарт Литтл!", black_list)
assert not has_black_list_words("уацуац", black_list)
assert has_black_list_words("Кот был смел и умел", black_list)
print("All tests passed")