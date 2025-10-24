def test_sum_value_of_the_same_key_kinds(d: dict) -> dict:
    final_lst = []
    year_lst = [(x[-4:], y) for (x, y) in list(d.items())]
    sum_of_year = year_lst[0][1]
    for cortej in range(len(year_lst) - 1):
        if year_lst[cortej][0] == year_lst[cortej + 1][0]:
            sum_of_year += year_lst[cortej + 1][1]
        else:
            final_lst.append((year_lst[cortej][0], sum_of_year))
            sum_of_year = year_lst[cortej + 1][1]
    final_lst.append((year_lst[-1][0], sum_of_year))
    return dict(final_lst)


monthly_sales = {
    "Jan_2020": 100,
    "Feb_2020": 90,
    "Mar_2020": 15,
    "Jan_2021": 10,
    "Feb_2021": 50,
    "Mar_2022": 5,
    "Sep_2023": 12,
    "Oct_2023": 12,
}
assert test_sum_value_of_the_same_key_kinds(monthly_sales) == {
    '2020': 205, 
    '2021': 60, 
    '2022': 5, 
    '2023': 24}
print("All tests passed")

