num = int(input("enter a number to get its divisors:"))
newlist = list(range(1,num))
print(newlist)
a = []
for number in newlist:
    if num % number == 0:
        a.append(number)

print(a) 





