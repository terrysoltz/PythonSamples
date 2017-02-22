# Python Drill, step 36
#
# Python Version: 2.7.13
#
# Author: Terry Soltz
#
# Purpose: Demonstrate use of basic Python syntax and structures
#


# Variable assignment

x = 5
name = "Terry"
y = 22.7

# Formatted printing

print("{} chose the numbers {} and {}.".format(name, x, y))

# Operators - Math

print("\n{} + {} = {}".format(x, y, x+y))
print("{} - {} = {}".format(y, x, y-x))
print("{} * {} = {}".format(x, y, x*y))
print("{} / {} = {}".format(y, x, y/x))
x += 1
print"x has been incremented, and now equals ", x
x = 5
print"x has been reset to ", x
print("{} Mod {} = {}".format(y, x, y%x))

# Operators - Logic

t = True
f = False
print("\n{} and {} is: {}".format(t, f, t and f))
print("{} or {} is: {}".format(t, f, t or f))
print("not {} is: {}".format(t, not t))

# Conditional statements

if x % 10 == 0:
    print("\n{} is a multiple of 10.".format(x))
elif x % 1 == 0:
    print("\n{} is not a multiple of 10, but is an integer.".format(x))
else:
    print("\n{} is not an integer".format(x))

# Use of while loop and use of list with for loop

x = 180
y = 2
z = x
result = []
while y <= z:
    if z % y == 0:
        result.append(y)
        z = z / y
    else:
        y += 1
print("\nPrime factors of {}:".format(x))
for i in result:
    print(i)

# Use of tuple and for loop

print("")
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for day in days:
    print(day)

# Function that returns a string

def getName():
    name = raw_input("\nWhat is your name? ").title()
    return name

print(getName())
