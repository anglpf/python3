# Import the argv function so that we can bring in a filename from the user
# in the command line.
from sys import argv

# Name the inputs from the command line.
script, filename = argv

# Open the file given by the user and make a 'file object' called txt
txt = open(filename)

# Print an f-string referencing the user's filename
print(f"Here's your file {filename}:")
print(txt.read()) # Use the function read() on our variable to read the file.

# Take an input from the user (using input() rather than argv)
print(f"Type the filename again:")
file_again = input('>>> ')

# Create another file object.
txt_again = open(file_again)

# Print their second file. (Maybe it's the same file.)
print(txt_again.read())

txt.close()
txt_again.close()
