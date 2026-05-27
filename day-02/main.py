print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill into? "))

bill_with_tip = total_bill * (1 + tip_percentage / 100)
amount_per_person = bill_with_tip / people_count

final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount}")