def hot_potato(players, n):
    circle = list(players)
    idx = 0

    while len(circle) > 1:
        idx = (idx + n - 1) % len(circle)
        removed_player = circle.pop(idx)
        print(f"Removed {removed_player}")

    winner = circle[0]
    print(f"Winner is {winner}")


players = input().split()
n = int(input())

hot_potato(players, n)