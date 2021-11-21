name = 'Angus Fudge'
age = 28
height = 74 # inches
weight = 78 # kgs
eyes = 'green'
teeth = 'off-white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He weighs {weight} kgs.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are {teeth}.")

total = age + height + weight
print(f"If I add my age, my height, and my weight, I get {total}.")

feet = height // 12
inches = height % 12

print(f"{name} is {feet} feet {inches} inches tall.")
print(f"{name} is {feet}\'{inches}\".")
