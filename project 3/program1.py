#program 1: limited loop
# Goal: print a list of grocery items to a user add a specific number of items to the list

#ask the user how many items they would like to add to their shopping list
shopping_list = []
count = int(input("How many items would you like to add to your shopping list? "))
print(f"Please enter your {count} items:").lower()
# the loop runs for the number of items specified by the user
for i in range(count):
    item = input(f"Item {i + 1}: ")
    shopping_list.append(item)
print("Here is your shopping list:")
for item in shopping_list:
    print("- " + item)