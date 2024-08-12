def _3palindrome():
    n = int(input())
    l = ("a a b b " * n).split()
    x = [l[i] for i in range(n)]
    x = "".join(x)
    print(x)


if __name__ == "__main__":
    _3palindrome()
