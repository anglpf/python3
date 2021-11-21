# this is like using argv
def print_two(*args):
    arg1, arg2 = args # similarity to argv following a reference to our variables
    print(f"arg1: {arg1}, arg2: {arg2}")

# the *args isn't necessary, we can do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Ango", "Wango")
print_two_again("Canada", "Goose")
print_one("Whistler")
print_none()
