import random 
number = int(input("Enter a number that you have guessed:"))
print("The number you have entered is", number)
for i in range(1):
    print ("the random number is",random.randint(1,9))

if i > number:
    print( "low")
elif i < number:
    print("You guessed high")
else:
    print("You guessed right")