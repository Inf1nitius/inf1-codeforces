n, k = map(int, input().split())
scores = [int(y) for y in input().split()]

i = sum(scores[x] > 0 and scores[x] >= scores[k - 1] for x in range(n))
print(i)
