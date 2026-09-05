n = int(input())

faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

total = 0

for i in range(n):
    name = input()
    total += faces[name]

print(total)