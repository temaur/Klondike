def get_views_count(n: int) -> str:
    if len(str(n)) == 1 and str(n) in "1":
        return f"{n} просмотр"
    if len(str(n)) == 1 and str(n) in "234":
        return f"{n} просмотра"
    if len(str(n)) == 1 and str(n) in "567890":
        return f"{n} просмотров"
    if len(str(n)) == 2 and str(n)[0] == "1":
        return f"{n} просмотров"
    if len(str(n)) > 1 and str(n)[-1] == "1":
        return f"{n} просмотр"
    if len(str(n)) > 1 and str(n)[-1] in "234":
        return f"{n} просмотра"
    if len(str(n)) > 1 and str(n)[-1] in "567890":
        return f"{n} просмотров"

assert get_views_count(0) == '0 просмотров'
assert get_views_count(1) == '1 просмотр'
assert get_views_count(9) == '9 просмотров'
assert get_views_count(11) == '11 просмотров'
assert get_views_count(14) == '14 просмотров'
assert get_views_count(21) == '21 просмотр'
assert get_views_count(22) == '22 просмотра'
assert get_views_count(25) == '25 просмотров'
assert get_views_count(1234) == '1234 просмотра'
assert get_views_count(100) == '100 просмотров'
print('All tests passed')
