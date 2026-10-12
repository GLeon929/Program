#Indefinite loop
# Goal: collect user names until the user wants to stop

print("Enter the names you want to add to the guest list.")
print("Type 'done' when you are finished.")
guest_list = []
user_input = ""
# the loop continues until the user types 'done'
while user_input.lower() != "done":
    user_input = input("Enter a name (or 'done' to finish): ")
    if user_input.lower() != "done":
        guest_list.append(user_input)

print("Here is the guest list:", guest_list)
