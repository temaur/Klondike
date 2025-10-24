def test_to_lists_to_dict(lst1: list[str], lst2: list[str]) -> dict:
    return dict(list(zip(lst1, lst2)))


keys = ["USA", "Russia", "France"]
income = [100, 10, 25, 45]


assert test_to_lists_to_dict(keys, income) == {'USA': 100, 'Russia': 10, 'France': 25}
print("All tests passed")
