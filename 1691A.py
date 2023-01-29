t = int(input())

for _ in range(t):
    n = int(input())
    alist = input().split()
    evens = 0
    odds = 0
    for a in alist:
        if int(a) % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(min(evens, odds))
