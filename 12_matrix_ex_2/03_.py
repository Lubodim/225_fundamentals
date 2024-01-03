n = int(input())
matrix = []

for r in range(n):
    matrix.append(input().split(", "))
    print(matrix)
for r in matrix:
    print(*r, sep=", ")