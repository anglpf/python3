# This exercise demonstrates a few concepts:
# How computers store languages for display and processing
# How you must encode and decode Python's strings into a type called bytes
# How to handle errors in strings and byte-handling
# How to read code and find out what it means even if I've never seen it before

import sys
script, input_encoding, error = sys.argv
# There are a few error inputs we can accept. 'strict' will generate an exception and fail. Other could e.g. replace unencodable unicode with a '?'.

def main(language_file, encoding, errors):
    # We use the parameter 'encoding', though Python refers to a codec.
    # Examples are utf-8, utf-16, big5.
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors) # Call the function below that runs on each line of the language file.
        return main(language_file, encoding, errors) # Go back to the main function and run it again. It will keep running for as long as there is another line to be read into the variable called line.

def print_line(line, encoding, errors):
    next_lang = line.strip() # strip() removes leading and trailing characters from a string input. E.g. line.strip(",.abc") would remove all instances of those 5 characters from the end of each line until reaching another type of character.
    raw_bytes = next_lang.encode(encoding, errors=errors) # If user inputs utf-8 as encoding, then this will encode the language name as utf-8
    cooked_string = raw_bytes.decode(encoding, errors=errors) # This decodes what we just encoded, using the same encoding. It should get us back to what we had, if our errors are strict.

    print(raw_bytes, "<===>", cooked_string) # When we print raw_bytes, we see a load of hexadecimal numbers for each byte, within a b'...' which indicates a byte-string. I guess this is like an f-string, but it's a b-string.


languages = open("languages.txt", encoding = "utf-8")

# utf-8 means Unicode Transformation Format 8 Bits. Generally, using 32 bits to store every character is a waste of space. But sometimes we need the extra to render less-frequent languages such as Lithuanian. utf-8 is a form of compression encoding that solves for this issue.

# Give the main function a file object (above), plus the user's argv inputs for encoding and error.
main(languages, input_encoding, error)

# If we run this script with big5 encoding, Python doesn't have much fun. That's because our language file has lots of other characters in it. To make it work, we have to change the error setting to 'replace' - then Python just fills in ? for all the characters it can't handle in big5.
