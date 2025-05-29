import random

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 5

    for i in range(rounds):
        print(f"\n--- Round {i + 1} ---")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("Your choice:", user_choice)
        print("Computer choice:", computer_choice)

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! No points awarded.")
            continue

        if computer_choice == user_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You got 1 point!")
            user_score += 1
        else:
            print("Computer got a point!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

    # Final Result
    print("\n=== Final Score ===")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("User won the game! ")
    elif computer_score > user_score:
        print("Computer won the game! ")
    else:
        print("It's a tie! ")

# Game Loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! ")
        break
