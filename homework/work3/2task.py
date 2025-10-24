def test_merge_two_dicts(dict1: dict, dict2: dict) -> dict:
    dict1.update(dict2)
    return dict1


developed_markets = {"USA": 100, "Russia": 25, "France": 45}
emerging_markets = {"Japan": 90, "Kazakhstan": 120, "India": 45}
assert test_merge_two_dicts(developed_markets, emerging_markets) == {
    "USA": 100,
    "Russia": 25,
    "France": 45,
    "Japan": 90,
    "Kazakhstam": 120,
    "India": 45,
}
print("All tests passed")

