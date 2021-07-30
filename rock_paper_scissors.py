import random

prompt = "Rock, Paper, or Scissors?"
prompt += "What is your choice? "

# Ask user for choice
player_choice = input(prompt)

# Make choice all lower case
player_choice = player_choice.lower()

# The computer will make a random choice
computer_choices = ['rock', 'paper', 'scissors']
number = random.randint(0,2)
computer_choice = (computer_choices[(number)])

## Logic goes here:
print(f"You chose: {player_choice.title()}. The computer chose {computer_choice.title()}.")
if player_choice == computer_choice:
    print("You both chose the same thing. It's a tie.")
if player_choice == 'rock' and computer_choice == 'paper':
    print("You lose.")
if player_choice == 'rock' and computer_choice == 'scissors':
    print("You win")
if player_choice == 'paper' and computer_choice == 'rock':
    print("You lose.")
if player_choice == 'paper' and computer_choice == 'scissors':
    print("You win")
if player_choice == 'scissors'and computer_choice == 'rock':
    print("You lose.")
if player_choice == 'scissors' and computer_choice == 'paper':
    print("You win")

