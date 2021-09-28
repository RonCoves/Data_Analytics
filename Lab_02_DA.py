# lab02#

sal = int(input("What is your salary? (Please enter value between 0 and 100) \n"))
kid1 = input("Do you have children? Y/N \n")
kid = kid1.upper()

if (30 <= sal < 50) and (kid == 'N'):
    print("Your Tax is 40")
elif (30 <= sal < 50) and (kid == 'Y'):
    print("Your Tax is 35")
elif (50 <= sal < 70) and (kid == 'N'):
    print("Your Tax is 50")
elif (50 <= sal < 70) and (kid == 'Y'):
    print("Your Tax is 45")
elif (sal < 30) and (kid == 'N'):
    print("Your Tax is 0")
elif (sal < 30) and (kid == 'Y'):
    print("Your Tax is 0")
elif (sal > 70) and (kid == 'Y'):
    print("Your Tax is 55")
elif (sal > 70) and (kid == 'N'):
    print("Your Tax is 55")
else:
    print("You entered incorrect data")
