import random

print("Welcome to Stone, Paper, Scissors Game!")
print("Choices: Stone, Paper, Scissors")

choices = ["Stone", "Paper", "Scissors"]

while True:
    # User Input
    user_choice = input("Enter your choice (Stone/Paper/Scissors): ").capitalize()
    if user_choice not in choices:
        print("Invalid choice, please choose Stone, Paper, or Scissors.")
        continue

    # Computer Random Choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the Winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")

    # Play Again?
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
