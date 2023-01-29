n = int(input())
x = input().split()

d = sum(i == "1" for i in x)

if d >= 1:
    print("hard")
else:
    print("easy")
