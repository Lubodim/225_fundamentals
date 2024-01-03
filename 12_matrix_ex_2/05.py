n=int(input())
matrix=[]
for row in range(n):
    matrix.append(list(map(int, input().split(", "))))

sld=0
for r in range(n):
    sld += matrix[r][r]
print(sld)