UserNumber = int(input("Enter a number:"))
print(UserNumber)

listRange = list(range(1,UserNumber+1))
newlist = []
for i in listRange:
    if UserNumber % i == 0:
        newlist.append(i)

print(newlist)


