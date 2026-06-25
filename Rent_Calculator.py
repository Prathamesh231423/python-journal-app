# Taking inputs from user
rent = float(input("Enter total rent: "))
food = float(input("Enter total food cost: "))
electricity_units = float(input("Enter electricity units consumed: "))
charge_per_unit = float(input("Enter charge per unit: "))
num_people = int(input("Enter number of people: "))

# Calculating electricity bill
electricity_bill = electricity_units * charge_per_unit

# Calculating total expense
total_expense = rent + food + electricity_bill

# Calculating per person share
per_person = total_expense / num_people

# Display results
print("\n----- BILL DETAILS -----")
print(f"Electricity Bill: ₹{electricity_bill}")
print(f"Total Expense: ₹{total_expense}")
print(f"Each Person Pays: ₹{per_person}")