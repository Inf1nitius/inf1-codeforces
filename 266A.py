n = int(input())
stones = input()
r = 0
g = 0
b = 0

for i in range(n - 1):
    if stones[i] == stones[i + 1]:
        if stones[i] == "R":
            r += 1
        elif stones[i] == "G":
            g += 1
        elif stones[i] == "B":
            b += 1

print(r + g + b)
