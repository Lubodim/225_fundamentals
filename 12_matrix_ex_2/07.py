# row, col = map(int, input().split(", "))
rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append(input().split(", "))

searched_symbol = input()

for row in range(rows):
    for col in range(cols):
        if searched_symbol == matrix[row][col]:
            print(f"{row}, {col}")
