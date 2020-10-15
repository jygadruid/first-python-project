import random
import time

def guess_random_4_numbers(lookingfor):
    num = 0
    i = 0
    while i <= 1:
        if num == lookingfor:
            print("Found " + str(lookingfor) + ", in " + str(num) + " tries.")
            return 
        else:
            print(num)
        num += 1

for x in range(1):
  randomint = random.randint(0, 9999)

print("The random integer is " + str(randomint))

time.sleep(5)

guess_random_4_numbers(randomint)