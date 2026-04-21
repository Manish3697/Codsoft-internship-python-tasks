import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Final Score -> You:", user_score, "| Computer:", computer_score)
        print("Game Over!")
        break