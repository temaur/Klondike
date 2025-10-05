def is_odd(n: int) -> bool:
  if n % 2 == 0:
    return True
  return False
  
assert is_odd(0)
assert is_odd(-14)
assert is_odd(14)
assert not is_odd(7)
print('All tests passed')