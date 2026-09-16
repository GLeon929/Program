# Get input rom the user
total_money_str = input("how much money do you have? >")
#Convert input strings to right number types
total_money = float(total_money_str)
number_of_days_str = input("how many days are you traveling? >")
number_of_days = int(number_of_days_str)
#do the conversion to calculate daily budget
daily_budget = total_money / number_of_days
print(f"Your daily budget is: {daily_budget} per day")
