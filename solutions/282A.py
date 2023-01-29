n = int(input())
x = 0

for statement in range(n):
    statement = input()
    op = statement.replace("X", "")
    if op == "++":
        x += 1
    elif op == "--":
        x -= 1

print(x)
