# Write a function named remainder() that has two parameters named num1 and num2. The function should return the remainder of twice num1 divided by half of num2.

# Write your remainder function here:
def remainder(num1, num2):
    num1doubled = num1 * 2
    num2halved = num2 / 2
    
    return num1doubled % num2halved

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0