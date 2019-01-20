userString = str(input("Enter a string:"))
print(userString)
print(userString[::-1])

if userString == userString[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")