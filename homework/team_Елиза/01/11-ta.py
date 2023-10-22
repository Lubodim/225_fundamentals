children = input().split()
n = int(input())

potato_list = list(range(len(children)))

while len(potato_list) > 1:
    loser = n % len(potato_list) - 1
    if loser < 0:
        loser = len(potato_list) - 1

    removed_child = potato_list.pop(loser)
    print(f"Removed {children[removed_child]}")
winner = potato_list[0]
print(f"Winner is {children[winner]}")