'''
QUESTION:

You are going to write a program that tests the compatibility between two people.
We're going to use the super scientific method recommended by BuzzFeed.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input
name1 = "Kanye West"
name2 = "Kim Kardashian"

Example Output
Your score is 42, you are alright together.

ANSWER:
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name_string = (name1+name2).lower()

t = name_string.count("t")
r = name_string.count("r")
u = name_string.count("u")
e = name_string.count("e")
true = t+r+u+e

l = name_string.count("l")
o = name_string.count("o")
v = name_string.count("v")
e = name_string.count("e")
love = l+o+v+e

true_love = int(str(true)+str(love))

if (true_love<10) or (true_love>90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love>=40) and (true_love<=50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")