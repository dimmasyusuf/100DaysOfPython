'''

QUESTION:

Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8

ANSWER:
'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

try:
    sum = int(two_digit_number[0]) + int(two_digit_number[1])
    print(f"Sum of digits of {two_digit_number} is {sum}")

except ValueError:
    print("Please enter a two digit number!")