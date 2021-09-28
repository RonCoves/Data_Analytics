#  Lab03#

#  ##### Question 1##########

print("*" * 8, "Question 1", "*" * 8)

print("Enter T for True OR F for False")
sal1 = input("My salary is greater 40? T/F \n")
sal = sal1.upper()
age1 = input("I am older then 25? T/F \n")
age = age1.upper()
work1 = input("I have worked for 25 years \n")
work = work1.upper()
kid1 = input("I have a child \n")
kid = kid1.upper()

if (sal == 'T' and age == 'T') or (work == 'T' and kid == 'T'):
    print("You can get a mortgage")
else:
    print("You cannot get a mortgage")
print("")
#  ##### Question 2##########

print("*" * 8, "Question 2", "*" * 8)
print("Enter T for True OR F for False")
sal1 = input("My salary is greater 40? T/F \n")
sal = sal1.upper()
age1 = input("I am older then 35? T/F \n")
age = age1.upper()
work1 = input("I have worked for 10 years \n")
work = work1.upper()
kid1 = input("I have a child \n")
kid = kid1.upper()

if (sal == 'T' or age == 'T') and (work == 'T' or kid == 'T'):
    print("You can get a mortgage")
else:
    print("You cannot get a mortgage")
print("")
