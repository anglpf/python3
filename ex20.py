from sys import argv

script, input_file = argv

# Function that reads a file object.
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

# Seek 0, having read the file.
rewind(current_file)

print("Then we print the lines separately:\n")

# Count the number of lines in the file
num_lines = len(current_file.readlines())

# Seek 0 having read the file.
rewind(current_file)

# Loop through the length of the file, printing the line number and line extract each time.
current_line = 0
for i in range(num_lines):
    current_line += 1
    print_a_line(current_line, current_file)
