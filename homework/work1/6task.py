def get_words(s: str) -> list[str]:
    return s.split(" ")


assert get_words("Александр Сергеевич Пушкин") == ["Александр", "Сергеевич", "Пушкин"]
assert get_words("Я поел лапши") == ["Я", "поел", "лапши"]
assert get_words("") == [""]
print("All tests passed")
