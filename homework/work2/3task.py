"""def clean_name(fio: str) -> str:
for s in fio:
    if (
        s
        not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ):
        fio = fio.replace(s, "")
return fio"""


def clean_name(fio: str) -> str:
    correct_symbols = (
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    )
    return "".join(list(filter(lambda x: x in correct_symbols, fio)))


assert clean_name("Ивqн Ив12yjdич") == "Ивн Ивич"
assert clean_name("") == ""
assert clean_name("grrjf 234n4f& rnfrnvы") == "  ы"
assert clean_name('Иван Иваныч!') == 'Иван Иваныч'
print('All tests passed')