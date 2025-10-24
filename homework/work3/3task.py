def test_sort_dict_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

emerging_markets = {
    "USA": 100,
    "Kazakhstan": 100,
    "Japan": 90,
    "France": 25,
    "China": 80,
    "India": 50,
    "Russia": 5,
}
assert test_sort_dict_values(emerging_markets) == {
    "USA": 100,
    "Kazakhstan": 100,
    "Japan": 90,
    "China": 80,
    "India": 50,
    "France": 25,
    "Russia": 5,
}
print('All tests passed')

# Мой первый вариант, но он не работает если у двух стран одинаковые значения
def test_sort_dict_values2(d: dict) -> dict:
    dict1 = {}
    for k, v in d.items():
        dict1[v] = k
    d = dict(sorted(dict1.items(), reverse=True))
    dict1.clear()
    for k, v in d.items():
        dict1[v] = k
    return dict1
emerging_markets = {
    "USA": 100,
    "Kazakhstan": 100,
    "Japan": 90,
    "France": 25,
    "China": 80,
    "India": 50,
    "Russia": 5,
}
print(test_sort_dict_values2(emerging_markets))
