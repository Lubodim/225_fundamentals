from collections import deque
from time import sleep
from random import choice

fighters = deque(
    ["Scorpion", "Liu Kang", "Sub Zero", "Kano",
     "Sonya Blade", "Raiden", "Baraka", "Jax",
     "Johnny Cage", "Kung Lao", "Jade",
     "Noob Saibot", "Kabal", "Geras", "D'Vorah",
     "Jacqui Briggs", "Scarlett", "Cassie Cage",
     "Kotal Kahn", "Erron Black"
     ]
)

print("Welcome to mortal combat game!")
print("Loading...", end="")
# sleep(2)
# for _ in range(5):
#     print(".", end="")
#     sleep(2)
# print()
counter = 0
player_name = input("Enter your Name: ")
player_blood = 100
strength = 80
player_power = strength
killed = []
comp_blood = 100
comp_str = range(20, 80)
comp_power = 0
is_continues = False
while True:
    if player_blood <= 0:
        print(f"{player_name} loose the Game\nGAME OVER")
        break
    if not fighters:
        print(f"{player_name} Win the GAME! You kill everyone!")
        break
    if is_continues:
        while True:
            question = input("Do you want to continue fight Y/N: ").upper()
            if question == "Y":
                print("Next fight!")
                break
            elif question == "N":
                print(f"{player_name} You kill {', '.join(killed)}!")
                exit()
            else:
                print("incorrect answer")
                continue
    is_continues = True
    computer = fighters.popleft()
    comp_strength = choice(comp_str)
    comp_power = comp_strength
    comp_blood = 100
    player_blood = 100
    while True:
        if player_blood <= 0:
            break
        if comp_blood < 0:
            break
        print(f"Will hit {player_name}")
        print(f"{player_name} have {strength} strength and {player_blood} blood")
        comp_blood -= (player_power - comp_strength) if player_power > comp_blood else 0
        if comp_blood <= 0:
            print(f"{player_name} Win the game!\n{computer} loose")
            strength += 5
            player_power += 5
            break
        print(f"Will hit {computer}")
        print(f"{computer} have {comp_strength} strength and {comp_blood} blood")
        if comp_power > strength:
            player_blood -= (comp_power - strength)
        else:
            player_blood -= comp_power / 2
        if player_blood <= 0:
            print(f"{player_name} Loose the Game!")
            break
    killed.append(computer)

print("UKTC")

# fatal
