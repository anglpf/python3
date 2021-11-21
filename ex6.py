types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
    # This is a 'formatted string literal' or 'f-string'.
    # It replaces the %s notation from previous Python versions.
    # If you remove the f, the string prints with the curly brackets and
    #  variable names.
    # You cannot have an empty set of curly brackets in an f-string.

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation) # Prints with the curly brackets, because it isn't formatted.
print(joke_evaluation.format(hilarious))
    # This is str.format(), which the internet notes is also older and worse
    # than using an f-string.

w = "This is the left side of ..."
e = "... a string with a right side."

print (w + e) # Adding strings will concatenate them.
