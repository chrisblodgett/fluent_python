from collections import abc


def show_count(count: int, word: str | None):
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return count_str + f' {word}s'


print(show_count(3, 'dog'))

# for python > 3.9 you can do list[str]


def tokenize(text: str) -> list[str]:
    return text.upper().split()


print(tokenize('m in g'))
