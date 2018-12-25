import random
import string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
length = 8
p =  "".join(random.sample(s,length ))
print(p)