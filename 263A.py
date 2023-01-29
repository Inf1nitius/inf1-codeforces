row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()
row5 = input().split()

matrix = [row1, row2, row3, row4, row5]

x = 0
y = 0

for row in matrix:
    for number in row:
        if number == "1":
            x = row.index("1") + 1
            y = matrix.index(row) + 1

print(abs(x - 3) + abs(y - 3))
