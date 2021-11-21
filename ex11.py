print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} years old, {height}, and {weight}. Correct?", end = ' ')
answer = input()

if answer.lower() in ['yes', 'yup', 'y', 'yarg', 'yessir', 'you betcha']:
    print("Boy, I'm clever.")
else:
    print("Seems I need some self-improvement.")
