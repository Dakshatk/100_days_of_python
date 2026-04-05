print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
number_of_people = int(input("How many people to split the bill?"))

bill_with_tip = bill * (tip/100) + bill


amt_per_person = bill_with_tip/number_of_people
final_amt = round(amt_per_person,2)

print(f"Each person should pay:{final_amt}")