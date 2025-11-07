def are_brackets_correct(s: str) -> bool:
    """
    Напишите функцию, которая возвращает true, если скобочная последовательность
    является правильной, т.е. все открывающиеся скобки соответствуют закрывающимся.
    Скобки могут быть круглыми и квадратными.
    ((( ))) - правильно.
    [][][] - правильно
    [()][] - правильно
    [(][)] - неправильно
    Темы: парсинг строк, стек (stack)
    """
    stack = []
    dict_brackets = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if stack == []:
                return False
            if stack.pop() != dict_brackets[c]:
                return False
    if stack != []:
        return False
    return True


assert are_brackets_correct("[][][]")
assert are_brackets_correct("((()))")
assert are_brackets_correct("[()][]")
assert not are_brackets_correct("[(][)]")
assert not are_brackets_correct("(()))")
assert not are_brackets_correct("((())")
print("All tests passed")
