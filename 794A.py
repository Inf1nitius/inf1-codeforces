a, b, c = map(int, input().split())
n = int(input())
y = list(map(int, input().split()))
x = sum(b < i and c > i for i in y)

print(x)
