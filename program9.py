import random
a = (random.randint(1,9))
user_guess = (random.randint(1,9))
print(a)
print(user_guess)
if a == user_guess:
    print("correct guess")
elif a > user_guess:
    print("too high")
else:
    print("print too low")


