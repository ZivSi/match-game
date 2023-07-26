"""
Created by Ziv Sion in 2022
You can use this code for whatever you want
Good luck!

Apple, Appel =
 100% length, 100% Same letters, 60% Order = 260 / 3 = 86%
"""


class LengthError(Exception):
    pass


def get_length_score(a: str, b: str):
    return round(min(len(a), len(b)) / max(len(a), len(b)), 1)


def get_letters_score(a: str, b: str):
    score = 1

    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            score -= 1 / len(b)

    return round(score, 1)


def get_order_score(a, b):
    score = 1

    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            score -= 1 / len(b)

    return round(score, 1)


def compare_words(a: str, b: str):
    if len(a) < 1 or len(b) < 1:
        raise LengthError("Length cannot be less than 1")

    length_score = get_length_score(a, b)
    letters_score = get_letters_score(a, b)
    order_score = get_order_score(a, b)

    try:
        return round((length_score + letters_score + order_score) * 100 / 3, 1)
    except ZeroDivisionError:
        return 0
