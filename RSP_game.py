#rock paper scissors game
import random

game = ("rock", "scissors", "paper")
running = True

while running:
    player = None
    computer = random.choice(game)

    while player not in game:
        player = input("Paper, Rock or Scissors?: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("Winner Winner!")
    elif player == "paper" and computer == "rock":
        print("Winner Winner")
    elif player == "scissors" and computer == "paper":
        print("Winner Winner")
    else:
        print("GEGEEE!!!")

    play_again = input("Wanna play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("See you later!")
