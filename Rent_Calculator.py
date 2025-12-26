#inputs form the user 
# total rent
#total food ordered for snacking
# electricity units consumed
# charge per unit
#no of people staying


# output
# total amount you've to pay is 

rent = int(input("Enter your hostel rent: "))
food = int(input("Enter total food amount: "))
units = int(input("Enter electricity units consumed: "))
charge_per_unit = int(input("Enter charge per unit of electricity: "))
no_of_people = int(input("Enter number of people staying: "))

total_electricity_charge = units * charge_per_unit
total_amount = rent + food + total_electricity_charge

print("Total amount you've to pay is:", total_amount//no_of_people)

