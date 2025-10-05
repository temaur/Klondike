def is_paliandrom(s: str) -> bool:
    lst = s.split(" ")
    new_s = "".join(lst)
    if new_s == new_s[::-1]:
        return True
    else:
        return False


assert is_paliandrom("а роза упала на лапу азора")
assert is_paliandrom("потоп потоп")
assert not is_paliandrom("очей очарование")
assert is_paliandrom('')
print("All tests passed")
