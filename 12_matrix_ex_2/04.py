n = int(input())
matrix = []
sum_m = 0
for r in range(n):
    row = list(map(int, input().split(', ')))
    matrix.append(row)
    sum_m += sum(row)

print(sum_m)
