"""This program lets us calculate the bmi using metric units"""


# 1st input: enter height in meters e.g: 1.65
height = float(input("Please enter your height in metres.\n"))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Please enter your weight in Kilograms.\n"))

# Below equation is the formula for calculating the bmi (w/h*h)
bmi = weight/ (height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:  
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")