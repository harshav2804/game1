import random

choice = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

def print_score():
    print(f"\nYour score: {user_score} | Computer score: {computer_score}")
    print("---------------------------------------------------------")

def play_round():
    global user_score, computer_score
    user_choice = input("Choose rock, paper, or scissor: ").lower()
    computer_choice = random.choice(choice)
    print(f"\nYou chose {user_choice.capitalize()}, computer chose {computer_choice.capitalize()}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You won this round!")
        user_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1

def check_winner():
    if user_score == 3:
        print("\nYou are the ultimate winner!")
        return True
    elif computer_score == 3:
        print("\nComputer is the ultimate winner!")
        return True
    return False

while True:
    play_round()
    print_score()
    if check_winner():
        break


    
