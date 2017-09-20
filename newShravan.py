#!/usr/bin/python3

import random

for i in range(0,100):
    print(str(i)+"."+str(random.randint(0,10000)))
    

print("shravan")
for i in range(0,100):
    print(str(i))

new  = 44
old  = 55
print(str(new))
print(str(old))
new,old = old,new
print(str(new))
print(str(old))

