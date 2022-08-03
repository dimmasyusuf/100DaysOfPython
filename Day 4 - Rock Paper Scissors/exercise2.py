'''
QUESTION:

You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string namesAsCSV into individual names and puts them inside a List called names.

Example Input
Angela, Ben, Jenny, Michael, Chloe

Example Output
Michael is going to buy the meal today!

ANSWER:
'''

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Long Form

# # Get the total number of items in list.
num_items = len(names)
# # Generate random numbers between 0 and the last index.
random_choice = random.randint(0, (num_items - 1))
person_who_will_pay = names[random_choice]

# # Short Form
# person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to pay for the meal today!")