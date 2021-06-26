import pytest


def get_fibonacci_number(n):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) <= n:
        new_element = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(new_element)
    return fibonacci_list[n]


@pytest.mark.parametrize('n, result', (
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (10, 55),
        (15, 610)
))
def test_fibonacci(n, result):
    assert get_fibonacci_number(n) == result
