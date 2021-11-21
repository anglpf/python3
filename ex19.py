def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} pieces of cheese.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print(f"That's enough for a party!")
    print("Get a blanket.\n")

# Run the function with direct number inputs
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Create integer-valued variables and use those in the function
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Run some maths within the function inputs.
print("We can do maths inside the function too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Call back the previous variables and apply some maths to them.
print("And, we can do maths on variables:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

user_cheese = int(input("How many pieces of cheese do you have? "))
user_crackers = int(input("How many boxes of crackers do you have? "))

cheese_and_crackers(user_cheese, user_crackers)
