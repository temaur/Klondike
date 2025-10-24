def test_fill_missed_years(d: dict) -> dict:
    int_lst = sorted([(int(x), y) for (x, y) in yearly_sales.items()])
    res = {}
    for i in range(len(int_lst) - 1):
        current_year, current_money = int_lst[i]
        next_year, next_money = int_lst[i + 1]
        year_diff = next_year - current_year
        money_diff = next_money - current_money
        if year_diff > 1:
            for j in range(1, year_diff):
                money_iteration = money_diff / year_diff
                res[current_year] = current_money
                res[current_year + j] = int(current_money + j * money_iteration)
        else:
            res[current_year] = current_money
    last_year, last_money = int_lst[-1]
    res[last_year] = last_money
    res = dict(sorted([(str(x), y) for (x, y) in res.items()]))
    return res


yearly_sales = {"2015": 50, "2018": 65, "2019": 120, "2023": 160}
assert test_fill_missed_years(yearly_sales) == {
    '2015': 50, 
    '2016': 55, 
    '2017': 60, 
    '2018': 65, 
    '2019': 120, 
    '2020': 130, 
    '2021': 140, 
    '2022': 150, 
    '2023': 160
    }
print("All tests passed")
