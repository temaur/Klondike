def get_pct_growth(lst: list) -> list:
    new_lst = [
        (f"{round(((lst[x+1] - lst[x]) / lst[x]) * 100)}%") for x in range(len(lst) - 1)
    ]
    new_lst.insert(0, None)
    return new_lst


assert get_pct_growth([100, 150, 300, 400]) == [None, "50%", "100%", "33%"]
assert get_pct_growth([100, 50, 200, 400]) == [None, "-50%", "300%", "100%"]
assert get_pct_growth([]) == [None]
print("All tests passed")
