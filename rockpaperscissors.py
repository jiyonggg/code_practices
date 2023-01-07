# A Rock Paper Scissors Game with CPU

import random

choices = ["Rock", "Paper", "Scissors"]
prey_dict = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

cpu_choice = random.choice(choices)
user_choice = None

while not user_choice:
    try:
        print("1: Rock\n2: Paper\n3: Scissors\n")
        num = int(input("Choice: "))

        if not num in (1, 2, 3): raise Exception
    except:
        print("\nInvalid Choice.\n")
        continue

    user_choice = choices[num - 1]

if user_choice == cpu_choice: print("\nDraw.")
else: print("Victory!") if cpu_choice == prey_dict[user_choice] else print("Defeat...")

print(f"\nYour Choice: {user_choice}\nCpu's Choice: {cpu_choice}")