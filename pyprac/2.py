#Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

UserNumber = int(input("Enter a number:"))
if (UserNumber % 2 == 0):
    print("Its an even number")
else:
    print("Its an odd number")

    