import math


def sinus(x: float, N: int=10) -> float:
    assert isinstance(x, (int, float))

    val = 0.
    n = 0
    for n in range(N):
        comp = math.pow(-1., n) * math.pow(x, 2 * n + 1) / math.factorial(2 * n + 1)
        val += comp

    return val
