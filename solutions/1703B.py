def icpc_balloons():
    t = int(input())
    for _ in range(t):
        n = input()
        s = list(input())
        s2 = set(s)
        print(len(s) + len(s2))


if __name__ == "__main__":
    icpc_balloons()
