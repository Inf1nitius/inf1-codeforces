n = int(input())

x = 0
d = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

for _ in range(n):
    s = input()
    x += d[s]

print(x)
