'''
QUESTION:

Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:
1. How you will store the user's input.
2. How you will generate a random choice for the computer.
3. How you will compare the user's and the computer's choice to determine the winner (or a draw).
4. And also how you will give feedback to the player.

ANSWER:
'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Player Chose: ")
print(choice[player_choice])

computer_choice = random.randint(0, 2)
print("Computer Chose: ")
print(choice[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice < computer_choice:
    print("You lose!")
elif player_choice == computer_choice:
    print("Draw!")