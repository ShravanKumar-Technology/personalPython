import random

ra = random.randint(0, 100)
gap = random.randint(0, 10)

print("random number is " + str(ra))

print("gap is " + str(gap))
for i in range(0, ra, gap):
    print(str(i))
