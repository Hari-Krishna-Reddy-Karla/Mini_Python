"""This program lets us calculate the bmi using metric units"""


# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

# Below equation is the formula for calculating the bmi (w/h*h)
print(int(float(weight)/float(height) ** 2))