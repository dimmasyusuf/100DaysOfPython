'''
QUESTION:

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight (kg) / height*height (m2)

Example Input
weight = 80
height = 1.75

Example Output
80 ÷ 1.75 x 1.75 = 26.122448979591837
26

ANSWER:
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

try:
    weight_as_int = int(weight)
    height_as_float = float(height)

    # # Using the exponent operator **
    bmi = weight_as_int / height_as_float ** 2

    # or using multiplication and PEMDAS
    # bmi = weight_as_int / (height_as_float * height_as_float)

    bmi_as_int = int(bmi)

    print(bmi_as_int)

except ValueError:
    print("Please enter the number only!")