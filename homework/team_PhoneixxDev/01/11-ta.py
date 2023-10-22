children = input("Enter names of children separated by spaces: ").split()
n = int(input("Enter the step number (n): "))

circle = list(children)  # Create a list of children's names
current_position = 0

while len(circle) > 1:
    current_position = (current_position + n - 1) % len(circle)
    removed_child = circle.pop(current_position)
    print(f"Removed {removed_child}")

winner = circle[0]
print(f"Winner is {winner}")