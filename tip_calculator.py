"""This program Helps in calculating tips"""

print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("What percentage tip would you like to give?\n"))
no_of_people = int(input("How many people to split the bill?\n"))

tip = total_bill * tip_percent / 100
bill_each = (total_bill + tip) / no_of_people

print(f'Each person should pay: {round(bill_each, 2)}')

# Alternative to round function
print(f'Each person should pay: {bill_each:.2f}')
