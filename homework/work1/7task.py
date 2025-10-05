def get_person_short_name(fio: str) -> str:
    lst = fio.split(' ')
    short_fio = ' '.join([x if x == lst[0] else x[0:1]+'.' for x in lst])
    return short_fio

assert get_person_short_name('Уразгалиев Темирлан Аскарович') == 'Уразгалиев Т. А.'
assert get_person_short_name('Катышев Максим Александрович') == 'Катышев М. А.'
assert get_person_short_name('') == ''
print('All tests passed')