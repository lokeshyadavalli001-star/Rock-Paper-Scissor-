import random
import time

player_score = 0
computer_score = 0
tie_score = 0

play_again = True

while play_again:
    print("Welcome to Rock Paper Scissors! Game")
    time.sleep(1)
    
    while True:
        user = input("Choose anything from these (r/p/s): ").lower()
        if user in ['r', 'p', 's']:
            break
        else:
            print("Invalid choice! Please choose from (r/p/s)")
    
    user_choice = user
    
    if user == 'r':
        user += '🪨'
    elif user == 'p':
        user += '📃'
    elif user == 's':
        user += '✂️'
    
    options = ['r🪨', 'p📃', 's✂️']
    
    print("Computer is choosing...")
    time.sleep(1)
    computer = random.choice(options)
    print("Processing...")
    time.sleep(1)
    print("Please wait...")
    time.sleep(1)
    
    if user == computer:
        print("It's a tie!")
        tie_score += 1
        print("You chosen " + user)
        print("Computer chosen " + computer)
    else:
        if user_choice == 'r':
            if computer == 's✂️':
                print("You won!")
                player_score += 1
            else:
                print("You lost")
                computer_score += 1
        elif user_choice == 'p':
            if computer == 'r🪨':
                print("You won!")
                player_score += 1
            else:
                print("You lost")
                computer_score += 1
        elif user_choice == 's':
            if computer == 'p📃':
                print("You won!")
                player_score += 1
            else:
                print("You lost")
                computer_score += 1
        
        print("You chosen " + user)
        print("Computer chosen " + computer)
    
    print(f"\n--- Current Scores ---")
    print(f"Player: {player_score} | Computer: {computer_score} | Ties: {tie_score}")
    print("----------------------\n")
    
    while True:
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        if play_again_input == 'y':
            play_again = True
            break
        elif play_again_input == 'n':
            print("Bye! Have a nice day!")
            print(f"\n=== Final Scores ===")
            print(f"Player: {player_score} | Computer: {computer_score} | Ties: {tie_score}")
            print("Thanks for playing! 🎮")
            play_again = False
            break
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")
