# lab01
########################################
# Q1
#######################################
print("*" * 8, "Question 1", "*" * 8)
ps1 = 'I Like "Python"'
ps2 = "I Like 'Python'"
print(ps1)
print(ps2)

name = input("What is your Name? \n")
age = int(input("What is your age? \n"))
print("Your name is", name, "you are", age, "years old")
print("")
##############################################
# Q3
#############################################
print("*" * 8, "Question 3", "*" * 8)
km = float(input("What is the distance in KM?\n"))
miles = km * 0.6214
print(km, "KM converted to miles is", miles, "miles")
print("")
#############################################
# Q4
############################################
print("*" * 8, "Question 4", "*" * 8)
fname = input("What is your First Name? \n")
sname = input("What is your Second Name? \n")
gd1 = int(input("What is your first grade? \n"))
gd2 = int(input("What is your second grade? \n"))
gd3 = int(input("What is your third grade? \n"))
avg = (gd1 + gd2 + gd3) / 3
print(fname, sname, "the average of your 3 grades is:", avg)

print("")
#############################################
# Q5
############################################
print("*" * 8, "Question 5", "*" * 8)
weight = int(input("What is your weight in lbs? \n"))
height = int(input("What is your height in inches? \n"))
sq = height * height
bmi = (weight / sq) * 703

print("Your BMI is:\n", bmi)
print("")

############################################
# Q6
############################################
print("*" * 8, "Question 6", "*" * 8)
cl_a = int(input("How many class A tickets were sold? \n"))
cl_b = int(input("How many class B tickets were sold? \n"))
cl_c = int(input("How many class C tickets were sold? \n"))
amm_a = cl_a * 20
amm_b = cl_b * 25
amm_c = cl_c * 30
tot = amm_a + amm_b + amm_c
print("The total amount generated from Class A tickets was:\n", amm_a)
print("The total amount generated from Class B tickets was:\n", amm_b)
print("The total amount generated from Class C tickets was:\n", amm_c)
print("The total amount generated was:\n", tot)
print("")

############################################
# Q7
############################################
print("*" * 8, "Question 7", "*" * 8)
name1 = input("What is your Name? \n")
age1 = int(input("What is your age? \n"))
mths = age1 * 12
days = age1 * 365
print(name1, "is", mths, "months old")
print(name1, "is", days, "days old")
print("")

############################################
# Q8
############################################
print("*" * 8, "Question 8", "*" * 8)
radius = float(input("Please enter the radius of the circle? \n"))
rad_sq = radius * radius
area = 3.14 * rad_sq
print("The area of the circle with radius", radius, "is", area)
print("The variable area is a ", type(area))
# Lab 01 End
