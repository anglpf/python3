formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "A ripple on a North Korean lake in which the farmers wade.",
    "A dribble from my water bottle waits in London's morning shade.",
    "Distant moments,",
    "Bound once made."
))
