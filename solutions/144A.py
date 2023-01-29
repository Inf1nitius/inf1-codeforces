n = int(input())
l = list(map(int, input().split()))
t = l.index(max(l))
l.reverse()
s = l.index(min(l))

x = s + t

if x >= n or n == 2 and x > 0:
    x -= 1
print(x)
