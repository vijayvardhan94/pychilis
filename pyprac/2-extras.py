#extras - If the number is a multiple of 4, print out a different message.

UserNumber = int(input("Enter a number:"))
if (UserNumber % 2 == 0):
    print("Its an even number")
    if (UserNumber % 4 == 0):
        print("Its a multiple of 4!")
else:
    print("Its an odd number")

#extras - If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 

num = int(input("Enter num:"))
check = int(input("Enter check:"))
if num % check == 0:
    print("It divides neat!")
else:
    print("They dont divide")