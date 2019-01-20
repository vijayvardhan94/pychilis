import random
a = random.sample(range(30), 10)
print(a)
b = random.sample(range(30), 10)
print(b)
c = []

for i in a:
    if i in b:
        c.append(i)
print(c)
