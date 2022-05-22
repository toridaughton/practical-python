import random

# roll = random.randint(1,6)

# guess = int(input("Guess the dice roll:\n"))

# if guess == roll:
#     print("Correct! They rolled a " + str(roll))
# else:
#     print("Wrong! They rolled a " + str(roll))


def roll_dice():
    dice_total = roll1 = random.randint(1, 6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rollled", roll1)
    print(player2, "rollled", roll2)


    if roll1 > roll2:
        (print(player1, "wins!"))
    elif roll2 > roll1:
        print(player2, "wins!")
    else:
        print("TIE!")

main()