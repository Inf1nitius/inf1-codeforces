numbers = input().split("+")
numbers.sort()
x = ""

for number in numbers:
    x += number
    x += "+"

x = x[:-1]

print(x)
