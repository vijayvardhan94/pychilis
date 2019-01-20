#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

UserName = str(input("Enter your Name:"))
UserAge = int(input("Enter your age:"))
AgeToHundred = 100 - UserAge
CurrentYear = 2018
YearOfHundred = CurrentYear + AgeToHundred
print(AgeToHundred,"years for you to reach age 100")
print(YearOfHundred, "is the year in which you will turn 100 years old")


