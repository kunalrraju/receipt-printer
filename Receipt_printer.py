item_list=[]
item_list_price=[]
item_list_quantity=[]
total_price=0
user_input=""

while(user_input!="done"):
    user_input=input("Enter the item names and type 'done' when you are done with all the items : ")

    if user_input=="done":
        continue

    item_price=float(input(f"Enter the price of {user_input} : $ "))
    item_quantity=int(input(f"Enter the quantity of {user_input} : "))
    item_list.append(user_input)
    item_list_price.append(item_price)
    item_list_quantity.append(item_quantity)

max_num_format=f"{max(item_list_price):.2f}"
format_value=3+len(str(max_num_format))

print(f"\n{'Receipt'}\n{'_'*58}")
print(f"{'No':<7}{'Items':<10} {'Quantity':<13} {'Unit price':<15} {'Total price'}")

for item_no in range(len(item_list)):
    print(f"{item_no+1}. {item_list[item_no]:>9} {item_list_quantity[item_no]:>9} {'$':>11} {item_list_price[item_no]:>1.2f} {'$':>{format_value+4}} {(item_list_price[item_no])*item_list_quantity[item_no]:>1.2f}")
    total_price+=(item_list_price[item_no])*item_list_quantity[item_no]

print('_'*58)
print(f"{'Total Price' : <50}$ {total_price:.2f}")