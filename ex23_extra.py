
print(chr(90))
# This produces the output " 'Z' ", since 90 is the unicode of Z.

print(chr(12345))
# The output is " '〹' " — no idea what that is!

print(ord('Z'))
# This produces the output 90.

normalText = "Learning Python the hard way."
abnormalText = "Leårning P¥thon thé hard wœy."

print(normalText)
print(abnormalText)

print(ascii(normalText)) # Returns the variable, but in single quotes, whereas the print command above has no quotes.
print(ascii(abnormalText)) # = 'Le\xe5rning P\xa5thon th\xe9 hard w\u0153y.''

print("Le\xe5rning P\xa5thon th\xe9 hard w\u0153y.") # Returns the same result as print(abnormalText).
