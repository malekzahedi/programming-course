# annotation
# docstring: document string


def is_vowel(value: str) -> bool:
    """ Returns if value is vowel or not."""
    return value.capitalize() in ('A','E','I','O','U')


def f(a: list, b: complex) -> list:
    ...


def g(a: bool = False) -> int:
    ...



def h() -> list[str]:
    ...


print()

is_vowel()


def f(a: int):
    if a> 10:
        return [1]
    else:
        return 3


def f(*args):
    ...
