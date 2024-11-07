def silnia_iter(n: int) -> int:
    val = 1
    for i in range(2, n + 1):
        val *= i

    return val


def silnia_rekur(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * silnia_rekur(n - 1)


if __name__ == "__main__":
    for n in range(10):
        print(n, silnia_iter(n), silnia_rekur(n))

