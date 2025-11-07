def get_longest_common_prefix(words: list[str]) -> str:
    common_prefix = words[0]
    for word in words[1:]:
        new_common_prefix = ""
        for i in range(min(len(common_prefix), len(word))):
            if common_prefix[i] == word[i]:
                new_common_prefix += common_prefix[i]
            else:
                break
        common_prefix = new_common_prefix
    return common_prefix


my_lst = ["flower", "flow", "flight"]


assert get_longest_common_prefix(my_lst) == "fl"
assert get_longest_common_prefix(['coventry', 'cover', 'covid']) == "cov"
print('All tests passed')