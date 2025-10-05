def is_prime(n: int) -> bool:
    if n <=1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
            break
    return True


assert not is_prime(4)
assert is_prime(19)
assert not is_prime(0)
assert not is_prime(1)
print("All tests passed")
