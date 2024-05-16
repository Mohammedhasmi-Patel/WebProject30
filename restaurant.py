'''
   we will make small mini project that doing that our customer can order anythibg and then we will ask again
   if our customer saying yes then more order will be added otherwise will sawing the total amount of bills.

'''


# we have to using dictionary to dishes and its value price 

menu={
  'Pizza':40,
  'Pasta':50,
  'Burger':60,
  'Salad':70,
  'Coffee':80
}

#Greet
print("Welcome to Hasmi's restaurant......")
print(" Pizza:Rs40\n Pasta:50\n Burger:60\n Salad:70\n Coffee:80")

#adding all total values 
order_total =0

item1 = input("Enter the item that u want to order.....")

if item1 in menu:
  order_total += menu[item1]
  print(f"Your item {item1} Added to your order....")

else:
  print("This item is not available not yet.....")


#now ask one more time to customer that he will adding something or not 

another_item = input("Do You want to add one more item?(yes/no)")
if another_item=="yes":
  item2 = input("Enter The order that you want to order.....")
  if item2 in menu:
    order_total+=menu[item2]
    print(f"Your item {item2} Added to your order....")
    
  else:
   print("This item is not available not yet.....")

print(f"Total Amount that You have to pay is {order_total}")