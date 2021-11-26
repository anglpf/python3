def add_numbers_up_to(start, end, increment, list):
    i = start
    while i < end:
        print(f"At the top i is {i}")
        list.append(i)
        i += increment
        print("List now: ", list)
        print(f"At the bottom i is {i}\n")

numbers = []

add_numbers_up_to(10, 26, 3, numbers)

print("The numbers: ")

for num in numbers:
    print(num)
