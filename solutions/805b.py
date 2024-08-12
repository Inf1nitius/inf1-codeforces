def _3palindrome():
    n = int(input())
    print("".join([("a a b b " * n).split()[i] for i in range(n)]))


if __name__ == "__main__":
    _3palindrome()
