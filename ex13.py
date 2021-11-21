from sys import argv
# read the WYSS section for how to run this:
# Instead of running 'python3.6 ex13.py' in the command line,
# include another three words afterwards,
# which will be read as the variables below.
# E.g. 'python3.6 ex13.py cypress grouse seymour' will output:
#   The script is called: ex13.py
#   Your first variable is: cypress
#   Your second variable is: grouse
#   Your third variable is: seymour

script, first, second, third, main = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

side = input("What's your favourite side? ")

print(f"Your order is {main} with a side of {side}.")
