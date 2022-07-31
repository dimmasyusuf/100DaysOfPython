'''
QUESTION:

If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Round the result to 2 decimal places.

ANSWER:
'''

try:
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    
    # Long Form
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_person = total_bill / people
    final_amount = round(bill_person, 2)
    print(f"Each person should pay: ${final_amount}")

    # Short Form
    # final_amount = round(((bill + (bill * (tip / 100))) / people), 2)
    # print(f"Each person should pay: ${final_amount}")

    # OR
    # final_amount = (bill / people) * ((100 + tip) / 100)
    # print(f"Each person should pay: ${round(final_amount, 2)}")

except ValueError:
    print("Please enter number only!")