#Rock paper scissor
import random

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def player_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        return player_choice()

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    player = player_choice()
    computer = computer_choice()
    print("You chose:", player)
    print("Computer chose:", computer)
    print(determine_winner(player, computer))

play_game()
