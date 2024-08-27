# menu={
#     'Pizza':40,
#     'Coffe':50,
#     'Burger': 60,
#     'Salad': 70,
#     'Passta' : 40,
# }
# print("Welcome To Our Resturant")
# print("Pizza: 40\nPasta:50\nCoffe:40\nBurger:60\nSalad:70")
#
# order_total=0
#
# item1=input("Enter the name of item you want to order : ")
# if item1 in menu:
#     order_total += menu[item1]
#     print(f"Your item is added succesfully item name is {item1}")
# else:
#     print("Please Order SomeThing else it is not available")
# another_order= input("Do you want add Another item (Yes/No) ")
# if another_order == "Yes":
#     item2=input("Enter the second item = ")
#     if item2 in menu:
#         order_total += menu[item2]
#         print(f"You {item2} is added Successfully")
#     else:
#         print("Please Order SomeThing else it is not available")
# print(f"The Total amount is {order_total}")
#

menu={
    'Pizza':40,
    'Coffe':50,
    'Burger': 60,
    'Salad': 70,
    'Pasta' : 40,
}
print("Welcome To Our Resturant")
print("Pizza: 40\nPasta:50\nCoffe:50\nBurger:60\nSalad:70")

order_total=0
user_order=input("Enter you Order : -")
if user_order in menu:
    order_total += menu[user_order]
    print("Your item is added successfully :")
    user_exit=input("Do you want to add some product (Yes/No) ")
    print("You Can Order  more 9 Product :")
    if user_exit == "Yes":
            for i in range(2,11):
               user_order2=input(f"Please enter product {i}:-")
               if user_order2 in menu:
                   print("Your Order is added successfully  ")
                   order_total += menu[user_order2]
                   print(f"Total Amount is {order_total}")
                   print("Please enter Exit for exit")
               elif user_order2 == "Exit":
                   print(f"Total Amount is {order_total}")
                   break

               else:
                   print("This product is not available:")

    else:
        print("Thank you for Ordering")
        print(f"Total Amount is {order_total}")
else:
    print("This product is not available:")








