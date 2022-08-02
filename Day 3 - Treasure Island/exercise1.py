'''
QUESTION:

Write a program that works out whether if a given number is an odd or even number.

Example Input 1
43

Example Output 1
This is an odd number.

Example Input 2
94

Example Output 2
This is an even number.

ANSWER:
'''

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")