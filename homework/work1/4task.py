def get_trangle_kind(a: int, b:int, c: int) -> str:
    if a == b == c:
        return 'равноберденный'
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        return 'равноcторонний'
    else:
        return 'обычный'
    
assert get_trangle_kind(4,4,4) == 'равноберденный'
assert get_trangle_kind(4,6,4) == 'равноcторонний'
assert get_trangle_kind(6,4,4) == 'равноcторонний'
assert get_trangle_kind(4,4,6) == 'равноcторонний'
assert get_trangle_kind(3,4,7) == 'обычный'
print('All tests passed')