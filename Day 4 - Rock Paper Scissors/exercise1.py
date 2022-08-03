'''
QUESTION:

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this.
But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1.
Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails

ANSWER:
'''

# Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")