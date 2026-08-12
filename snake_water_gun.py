"""
Snake, Water, Gun
A hand-game where you play against the computer.
Rule: snake drinks water, water rusts gun, gun kills snake.
"""

import random

CHOICES = {"s": 1, "w": 0, "g": -1}
NAMES = {1: "snake", 0: "water", -1: "gun"}
# (winner, loser) pairs
BEATS = {(1, 0), (0, -1), (-1, 1)}


def play():
    comp = random.choice([-1, 0, 1])
    you_str = input("enter your choice (s = snake, w = water, g = gun): ").strip().lower()

    if you_str not in CHOICES:
        print("Please enter s, w, or g.")
        return

    you = CHOICES[you_str]
    print(f"you chose {NAMES[you]}\ncomp chose {NAMES[comp]}")

    if comp == you:
        print("it's a draw")
    elif (you, comp) in BEATS:
        print("you win!")
    else:
        print("you lose")


if __name__ == "__main__":
    play()
