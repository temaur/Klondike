def reverse_words(input_str: str) -> str:
    lst = input_str.split()
    return " ".join(lst[::-1])


s = "the sky is blue"


assert reverse_words(s) == "blue is sky the"
assert reverse_words("Hello, how are you?") == "you? are how Hello,"
print("All tests passed")
