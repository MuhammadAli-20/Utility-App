# Step:1 Display items information.
list_of_items = {

111:{"Product_name": "Chocolate", "type": "- Snack", "Cost": 2.00, "Available": 5},

112:{"Product_name": "Juice", "type": "- Drink", "Cost": 1.50, "Available": 7},

113:{"Product_name": "Chips", "type": "- Snack", "Cost": 2.75, "Available": 12},

114:{"Product_name": "Ice cream", "type": "- Snack", "Cost": 3.00, "Available": 18},

115:{"Product_name": "Milk", "type": "- Drink", "Cost": 1.00, "Available": 14},

116:{"Product_name": "Hot chocolate", "type": "- Drink", "Cost": 3.50, "Available": 11},

                 
                 }

# Step:2 Present the list of items.
print("\tVending Machine")
for list, info in list_of_items.items():
    print(f"{list} {info["Product_name"]} {info["type"]}\n ({info["Cost"]:.2f}\n {info["Available"]}") 

import time

answer = input("Would you like to use the vending machine? [Yes or No]: ")
if answer == "Yes".lower():
        print("\vAlright, you may choose an item of your choice.")
else:
   quit()

# Step:3 Code information.
code_of_item = int(input("\vEnter the correct code of the item: "))
if code_of_item in list_of_items:
        print("\vCorrect code.")

# Step:4 Available items in stock.
chosen_item = list_of_items[code_of_item]
if chosen_item["Available"] == 0 or chosen_item["Available"] <= 0:
   print(f"The \v{chosen_item["Product_name"]} is not available anymore.")

# Step:5 Money procedure.
amount = float(input("\vEnter the money here: "))
print(f"\vYour inserted amount is: {amount:,.2f}")

Proceed = input("\vDo you want to proceed?: ")

if amount < chosen_item["Cost"]: 
   print("\vYou inserted an incorrect amount.")
   quit()

if Proceed.lower() == "yes":
   print(f"\vAlright, The cost of {chosen_item['Product_name']} is {chosen_item['Cost']:,.2f}.")
else:
   exit()

Final_amount = amount - chosen_item["Cost"]
chosen_item["Available"] -=1

time.sleep(3)
print(f"\vHere is your {chosen_item['Product_name']}.")

if Final_amount != 0:
   print(f"\vYour final amount is {Final_amount:,.2f}.") # Step:6 Total amount after purchasing.
   print("\v\tThankyou for purchasing an item.")










       



       















































