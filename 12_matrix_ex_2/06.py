n = int(input())
matrix = []
for _ in range(n):
     row = list(map(int, input().split(', ')))
     matrix.append(row)

diagonal = sum(matrix[i][n - 1 - i] for i in range(n))

print(diagonal)
