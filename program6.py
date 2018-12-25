user_string = str(input("enter a string:"))
print("the string entered is:", user_string)
if user_string[::-1]== user_string:
    print("string entered is a palindrome")
else:
    print("string entered is not a palindrome")