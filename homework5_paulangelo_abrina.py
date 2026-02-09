# List Exercise
# 1. Create a list that contains 6 items
my_list = ["item1", "item2", "item3", "item4", "item5", "item6"]
# 2. Print the items in the list to the output console
print(my_list)
# 3. Print the first two items using a slice
print("The first two items in the list are:", my_list[0:2])
# 4. Print the middle two items using a slice
print("The middle two items in the list are:", my_list[2:4])
# 5. Print the first and last items using indexes
print("The first and last items in the list are:", my_list[0], my_list[5])


# Tuple Exercise
# 1. Create a tuple with five basic foods
menu = ("pizza", "burger", "salad", "pasta", "soup")
# 2. Print each item using a for loop
for food in menu:
    print(food)
# 3. Copy the tuple, replacing two items
menu = ("pizza", "burger", "tacos", "pasta", "sandwich")
# 4. Print each item on the revised menu
for food in menu:
    print(food)
    