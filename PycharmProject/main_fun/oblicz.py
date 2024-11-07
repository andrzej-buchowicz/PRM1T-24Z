import sys

from silnia import silnia_iter


def main():
    for param in sys.argv[1:]:
        n = int(param)
        print(n, silnia_iter(n))


if __name__ == "__main__":
    main()
