# Here are some methods/functions we can give to files:
# close - closes the file, like File/Save in your editor.
# read - read the file. You can assign the result to a variable
# readline - reads just one line of a text file.
# truncate - empties the file. Use with caution.
# write('stuff') - writes what's in the quotes to the file.
# seek(0) - moves to the beginning of the file.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit ^C.")
print("If you do want to do that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+')
# 'w' opens the file in write mode
# 'r' opens the file in read mode
# 'a' opens the file in append mode
# 'r+' and 'a+' allow read and write
#   r+ will begin at start of file until you read it once
#   a+ will begin at end of file (ready to append straight away)

target.seek(0)
print("After opening, the file says: \n", target.read())

print("Truncating the file. Goodbye!")
target.truncate()

target.seek(0)
print("After truncating, the file says: \n", target.read())

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.seek(0)
print("After writing, the file says: \n", target.read())

print("And now we close the file.")
target.close()
