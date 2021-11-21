tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print("'{}'".format(tabby_cat), "said the Tabby Cat.")
print("'{}'".format(persian_cat), "said the Persian Cat.")
print("'{}'".format(backslash_cat), "said the Backslash Cat.")
print("'{}'".format(fat_cat), "\nsaid the Fat Cat.")
