import random

prompt = "Rock, Paper, or Scissors?"
prompt += "What is your choice? "

# Ask user for choice
player_choice = input(prompt)

# Make choice all lower case
player_choice = player_choice.lower()

# The computer will make a random choice
computer_choices = ['rock', 'paper', 'scissors']
number = random.randint(0,3)
computer_choice = (computer_choices[(number)])

## Logic goes here:



