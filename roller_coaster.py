"""This program teaches how to use if/else statements"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
        
    wants_photo = input("Would you like your picture taken? Y or N.\n")
    if wants_photo == 'Y' or wants_photo == 'y':
        bill += 3
    print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    

    