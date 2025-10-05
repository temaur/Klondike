def is_arifm_progression(a: int, b: int , c: int) -> bool:

  if b-a == c-b:
    return True
  return False
  
assert is_arifm_progression(2,4,6)
assert not is_arifm_progression(4,57,222)
print('All tests passed')
